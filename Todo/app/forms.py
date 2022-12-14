from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2']
        
        
        
class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'