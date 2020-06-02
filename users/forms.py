from django import forms
from .models import *


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['email', 'phone', 'first_name', 'last_name']
