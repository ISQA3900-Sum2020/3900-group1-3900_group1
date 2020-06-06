from . import views
from django.urls import path, re_path, include

app_name = 'users'

urlpatterns = [
    re_path(r'register_customer/', views.register_customer, name='register_customer'),
    path('edit/<int:pk>', views.edit_customer, name='edit_customer'),
]