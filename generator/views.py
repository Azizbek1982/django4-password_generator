import random
import string
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = string.ascii_lowercase
    if request.GET.get('uppercase'):
        characters += characters.upper()
    if request.GET.get('special'):
        characters += string.punctuation
    if request.GET.get('numbers'):
        characters += string.digits
    length = int(request.GET.get('length'))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


def info(request):
    return render(request, 'generator/info.html')

