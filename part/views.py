from django.shortcuts import render
from . models import des
from . models import coments
from django.contrib.auth.models import User

def sum(request,id):  #fetch the product using id
	dests=des.objects.filter(id=id)
	return render(request,'sum.html',{'dests':dests[0]})




def index(request): # display all data
	dests=des.objects.all()
	return render(request,'index2.html',{'dests':dests})




def acc(request):
	dests=des.objects.all()
	return render(request,'acc.html',{'dests':dests})


def con(request):
	dest=request.GET.get('text','Default');
	pest=request.GET.get('name','Default');
	print(dest)
	commen=coments.objects.create(name=pest,comments=dest)
	commen.save()
	return render(request,'contact.html',{'commen':commen})

def gal(request):
	return render(request,'gallery.html')