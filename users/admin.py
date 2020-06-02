from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeCreateForm, EmployeeUpdateForm
from .models import Employee


class EmployeeAdmin(UserAdmin):
   add_form = EmployeeCreateForm
   form = EmployeeUpdateForm
   model = Employee
   list_display = ['email', 'username','phone' ,'is_staff','is_superuser' ]


admin.site.register(Employee, EmployeeAdmin)
