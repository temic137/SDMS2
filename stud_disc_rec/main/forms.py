from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student 

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['Stud_ID', 'FName', 'LName', 'Dept', 'Levl', 'Phone_No', 'Next_of_Kin', 'password', 'Next_of_Kin_Phone_No']



class AdminCheckForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)