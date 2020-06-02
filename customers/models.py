from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    cust_id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
    username = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('customer_detail', args=[str(self.cust_id)])