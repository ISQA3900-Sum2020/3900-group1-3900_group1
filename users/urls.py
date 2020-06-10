from . import views
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    re_path(r'register_customer/', views.register_customer, name='register_customer'),
    path('edit/<int:pk>', views.edit_customer, name='edit_customer'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('contact_page/', views.visitor_new, name='visitor_new'),
    path('about_page/', views.about, name='about'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('faq_page/', views.faq, name='faq'),
]
