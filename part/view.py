from django.shortcuts import render,redirect

from . models import des
from django.contrib import messages



def search(request):
		if request.method=='GET':
			place=request.GET.get('where')
		
		if place:
			match=des.objects.filter(name__icontains=place)

			if match:
				return render(request,'search.html',{'sr':match})
			else:
				messages.info(request,'Sorry No Result Found')
				return redirect('/search/')

		
			
		else: 
			return render(request,'search.html')