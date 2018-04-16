from django import forms
from .models import CustomUser
from django import forms

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'birth_date']
        widgets = {
            'password': forms.PasswordInput(),
            'birth_date': forms.SelectDateWidget(years=range(1900, 2018)),
        }