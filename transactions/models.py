from django.db import models
from django.contrib.auth.models import User




class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Bills', 'Bills'),
        ('Salary', 'Salary'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other')
    ]

    TYPE_CHOICES = [
        ('Income', 'Income'),
        ('Expense', 'Expense')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length = 50, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length = 10, choices=TYPE_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    
