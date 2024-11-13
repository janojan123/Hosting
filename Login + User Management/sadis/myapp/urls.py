from django.urls import path
from django.shortcuts import redirect, render  # Import redirect and render here

from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect to login
    path('login/', views.login_view, name='login'),
    path('success/', lambda request: render(request, 'success.html'), name='success_page'),
    path('users/', views.user_list, name='user_list'),  # Read (List all users)
    path('users/create/', views.user_create, name='user_create'),  # Create (Add a new user)
    path('users/detail/<int:id>/', views.user_detail, name='user_detail'),  # Update (Edit a user)
    path('users/update/<int:id>/', views.user_update, name='user_update'),  # Update (Edit a user)
    path('users/delete/<int:id>/', views.user_delete, name='user_delete'),  # Delete (Remove a user)
    path('accounting/', views.accounting, name='accounting'),  # Accounting page
    path('report/', views.report_view, name='report'),  # Report page
    path('ledger/', views.ledger_view, name='ledger'),  # Ledger pag
    path('vendor/', views.vendor_view, name='vendor'),  # Vendor page
    path('customer/', views.customer_view, name='customer'),  # Customer page
    path('logout/', views.logout_view, name='logout'),  # Logout
]
