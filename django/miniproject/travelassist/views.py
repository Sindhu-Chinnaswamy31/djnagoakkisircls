from django.shortcuts import render#(print data)

# Create your views here.
#create with html response
from django.http import HttpResponse
#def index(request):
	#return HttpResponse("<h1 style='text-align:center;color:red;background-color:gray'>Welcome to django</h1>")
def index(request):
	return render(request,"travel/index.html")

def contact(request):
	return render(request,"travel/contact.html")

def about(request):
	return render(request,"travel/about.html")

#def aboutus(request):
	#return HttpResponse("<h1 style='text-align:bottom;color:pink;background-color:blue'>Welcome to our page</h1>")

