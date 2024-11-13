from django import forms
from myapp.models import TblUser,TblCustomer

class UserForm(forms.ModelForm):
    class Meta:
        model = TblUser
        fields = ['username', 'password', 'name', 'email', 'role']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = TblCustomer
        fields = ['retail_name', 'address', 'email', 'phone_number']  # Specify the fields you want to update