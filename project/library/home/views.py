# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout

# Create your views here.

def home(request):
    return render(request , 'home/home.html')

def Login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request , user)
            return redirect ('/home/')
        else:
            args = {'message':'username does not exits or password is incorrect'}
            return render(request , 'home/login_page.html' , args)
    else:
        return render (request, 'home/login_page.html')

def register(request):
    args={}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirm_password']
        if password != password2:
            args  = {'message': 'password does not match'}
            return render(request, 'home/login_page.html' ,args)
        else:
            User.objects.create_user(username = username , password = password)
            return redirect ('/home/')
    else:
        return render(request, 'home/signup.html')
    