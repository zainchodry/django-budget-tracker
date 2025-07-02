from django.shortcuts import render, redirect
from django.views import View
from . forms import *
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
# Create your views here.


class Signup(View):
    def get(self, request):
        form = RegistrationForm()
        context = {
            'form':form
        }
        return render(request,"register.html", context)
    
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = RegistrationForm()
        context = {
            'form':form
        }
        return render(request, "register.html", context)
    



def logout(request):
    auth_logout(request)
    messages.success(request, "You Logout Succesfully")
    return redirect('login')
