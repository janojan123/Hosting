from django.urls import path
from django.shortcuts import redirect, render  # Import redirect and render here

from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect to login
    path('login/', views.login_view, name='login'),
    path('success/', lambda request: render(request, 'success.html'), name='success_page'),
    path('users/', views.user_list, name='user_list'),  # Read (List all users)
    path('users/create/', views.user_create, name='user_create'),  # Create (Add a new user)
    path('users/update/<int:id>/', views.user_update, name='user_update'),  # Update (Edit a user)
    path('users/delete/<int:id>/', views.user_delete, name='user_delete'),  # Delete (Remove a user)
    path('accounting/', views.accounting, name='accounting'),  # Accounting page
    path('report/', views.report_view, name='report'),  # Report page
    path('ledger/', views.ledger_view, name='ledger'),  # Ledger page
    path('vendor/', views.vendor_list, name='vendor_list'),  # Vendor page
    path('vendors/', views.vendor_list, name='vendor_list'),  # List all vendors
    path('vendor/create/', views.vendor_create, name='vendor_create'),  # Create a new vendor
    path('vendor/<int:id>/', views.vendor_detail, name='vendor_detail'),  # Detail view for vendor
    path('vendor/<int:id>/update/', views.vendor_update, name='vendor_update'),  # Update view for vendor
    path('vendor/<int:id>/delete/', views.vendor_delete, name='vendor_delete'),  # Delete view for vendor
    path('customers/', views.customer_list, name='customer_list'),  # List all customers
    path('customer/create/', views.customer_create, name='customer_create'),  # Create a new customer
    path('customers/<int:id>/', views.customer_detail, name='customer_detail'),  # Detail view for customer
    path('customers/<int:id>/update/', views.customer_update, name='customer_update'),  # Update view
    path('customers/<int:id>/delete/', views.customer_delete, name='customer_delete'),  # Delete view
    path('logout/', views.logout_view, name='logout'),  # Logout
]
