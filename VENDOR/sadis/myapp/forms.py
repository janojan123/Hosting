from django import forms
from myapp.models import TblUser, TblCustomer, TblVendor

class UserForm(forms.ModelForm):
    class Meta:
        model = TblUser
        fields = ['username', 'password', 'name', 'email', 'role']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = TblCustomer
        fields = ['retail_name', 'address', 'email', 'phone_number']  # Specify the fields you want to update

class VendorForm(forms.ModelForm):  # New form for TblVendor
    class Meta:
        model = TblVendor
        fields = ['company_name', 'address', 'email', 'phone_number', 'contract_period']  # Specify the fields for vendor
