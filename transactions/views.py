from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.db.models import Sum
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user = request.user).order_by('-date')
    income = transactions.filter(type = 'Income').aggregate(total=Sum('amount'))['total'] or 0
    expense = transactions.filter(type = 'Expense').aggregate(total = Sum('amount'))['total'] or 0
    balance = income - expense

    monthly_summary = {}
    for txn in transactions:
        month = txn.date.strftime('%B %Y')
        if month not in monthly_summary:
            monthly_summary[month] = {'income': 0, 'expense': 0}
        if txn.type == 'Income':
            monthly_summary[month]['income'] += txn.amount
        else:
            monthly_summary[month]['expense'] += txn.amount

    context = {
        'transactions':transactions,
        'income':income,
        'expense':expense,
        'balance':balance,
        'monthly_summary':monthly_summary
    }
    return render(request, "dashboard.html", context)


@login_required
def add_transaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        txn = form.save(commit = False)
        txn.user = request.user
        txn.save()
        messages.success(request, "Form Submitted Successfully !")
        return redirect('dashboard')
    return render(request,'add_transaction.html',{'form':form})



@login_required
def delete_transaction(request, id):
    txn = Transaction.objects.get(pk = id, user=request.user)
    txn.delete()
    return redirect('dashboard')



