from django.urls import path
from . views import *


urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('add/', add_transaction, name='add_transaction'),
    path('delete/<int:id>/',delete_transaction, name='delete_transaction'),
]