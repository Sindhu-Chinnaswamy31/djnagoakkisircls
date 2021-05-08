from django.shortcuts import render
from App.models import Customer_data
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def package1(request):
    return render(request,'package1.html')

def save_data(name,email,phno,sub,mes,comment=""):
    d=Customer_data.objects.get_or_create(Name=name,Email=email,PhoneNo=phno,Subject=sub,Message=mes,Comment=comment)[0]
    d.save()


def contacts(request):
    if request.method=="POST":
        data=request.POST
        save_data(name=data['name'],email=data['email'],phno=data['phno'],\
            sub=data['subject'],mes=data['review'])
        subject="New Registration"
        message="""
        Name={}
        Email={}
        PhoneNo={}
        Subject={}
        Message={}""".format(data['name'],data['email'],data['phno'],\
            data['subject'],data['review'])
        from_mail="akshayvk64@gmail.com"
        to=[from_mail]
        send_mail(subject,message,from_mail,to,fail_silently=False)
        #print(data['review'])
    return render(request,'contact.html')


def services(request):
    return render(request,'services.html')

def faq(request):
    return render(request,'faq.html')

def gallery(request):
    return render(request,'gallery.html')
