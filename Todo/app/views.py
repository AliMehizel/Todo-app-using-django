from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegisterForm,NoteForm
from .models import Note

# Create your views here.


def base(request):
    return render(request, 'base.html')

def LoginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        auth_user = authenticate(request, username=username, password=password)
        if auth_user is None:
        
           return redirect('/login/')
        else: 
           login(request,auth_user)
           return redirect('/note/')
             
    return render(request, 'login.html')

def SignupUser(request):
    form = {'RigsterForm': RegisterForm()}
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            login(request, new_user)
            return redirect('/note/')
        else:
            user_form = RegisterForm()
    return render(request, 'signup.html', form)

def CreateNote(request):
    form_note = {'form_note': NoteForm()}
    if request.method == 'POST':
        auth = request.user
        text = request.POST['text']
        note = NoteForm(request.POST)
        if note.is_valid():
            valid_note = Note.objects.create(auth = auth, text = text)
            valid_note.save()
            return redirect('/note/')
    return render(request, 'noteCreate.html', form_note)

def ListNote(request):
    note = Note.objects.all()
    objects = {'objects': note}
    return render(request, 'note.html', objects)
    

def UpdateNote(request, pk):
    note = {'note': Note.objects.get(pk=pk)}
    return render(request,'updatenote.html', note)

def Updated(request, pk):
    text = request.POST['text']
    note = Note.objects.get(pk=pk)
    note.text = text
    note.save()
    return redirect('/note/')

def DeleteNote(request, pk):
    note_delete = Note.objects.filter(pk=pk)
    note_delete.delete()
    return redirect('/note/')
    