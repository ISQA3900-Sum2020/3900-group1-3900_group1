from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="customer")

    def __str__(self):
        return self.user.username


class visitor(models.Model):
    cust_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.cust_name)
