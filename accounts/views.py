from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def log(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect("/")

		else:
			messages.info(request,'invaild')
			return redirect('/login/')
	return render(request,'login.html')

def reg(request):
	if request.method=="POST":
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
	

		user=User.objects.create_user(username=username,password=password1, email=email)
		user.save()
		messages.info(request,'Account created successfully')
		return redirect('/')

	else:
		return render(request,'register.html')

def logout(request):
	auth.logout(request)
	return redirect('/')
