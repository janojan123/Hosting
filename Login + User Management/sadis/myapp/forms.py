from django import forms
from myapp.models import TblUser

class UserForm(forms.ModelForm):
    class Meta:
        model = TblUser
        fields = ['username', 'password', 'name', 'email', 'role']
