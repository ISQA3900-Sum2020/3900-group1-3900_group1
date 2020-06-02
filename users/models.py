from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    emp_Id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50, default=' ', null=True, blank=True)