from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

app_name = 'shop'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('category/create/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/view/', views.category_list, name='category_list'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('shop/employee_home/', views.employee_home, name='employee_home'),
    path('shop/home/', views.home, name='home'),
    path('shop/contact_page/', views.visitor_new, name='visitor_new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)