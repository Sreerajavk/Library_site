

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from polls.models import todo
from polls.form import Postform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def index(request):
	
    return HttpResponse("hai sreeraj")
def post_form_upload(request):
	if request.method=='GET':
		form=Postform()
	else:
		form=postform(request.POST)
		
def log(request):
	data={}
	if request.method=="POST":
		username=request.POST.get("user")
		password=request.POST.get("pass")
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user) 
			return redirect("/todo")
		else:
			return render(request,"login.html",{"message":"username does not exits"})
	else:
		return render(request,"login.html",data)
def sree(request):
	l=['ss','dd']
	data={"names":l}
	return render(request,"sree.html",data)
def signup(request):
	data={}
	if request.method=="POST":
		username=request.POST.get("user")
		password=request.POST.get("pass")
		cpassword=request.POST.get("confirmpass")
		if password!=cpassword:
			return render(request,"signup.html",{"message":"password does not match"})
		else:
			user=User.objects.create_user(username=username,password=password)
			return redirect("/login")
	else:
			return render(request,"signup.html",data)
	
def to(request):
	
	l=[]
	item=request.POST.get("input")
	l.append(item)
	data={"items":l}
	return render(request,"todo.html",data)
	
def log_out(request):
	pass
	
	