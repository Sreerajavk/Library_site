# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect      
from django.contrib.auth import login , authenticate
# Create your views here.

def index(request):
    return HttpResponse("<h1>hey there</h1>")

def home(request):
    return render(request , 'home.html')

def login(request):
        data={}
	if request.method == "POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=authenticate(username=username,password=password)
		if user is not None:
			login(user) 
			return redirect("/home")
		else:
			return render(request,"login_page.html",{"message":"username and password does not match"})
	else:
		return render(request,"login_page.html",data)


from .form import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

