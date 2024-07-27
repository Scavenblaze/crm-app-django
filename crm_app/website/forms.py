from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

#Register Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



#Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(label="", required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label="", required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(label="", required=True, widget=forms.widgets.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone = forms.CharField(label="", required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    address = forms.CharField(label="", required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    city = forms.CharField(label="", required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(label="", required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipcode = forms.CharField(label="", required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Zip Code', 'class': 'form-control'}))
    
    class Meta:
        model = Record
        exclude = ("user",)
    
    