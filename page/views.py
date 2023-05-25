from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post

def home(request):
   return render(request, "home.html")
