from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):

     
    ex=Experts.objects.all()
    return render(request, 'landingpage.html',{'ex':ex})
def login(request):
    return render(request, 'login.html')
def register(request):
        # if request.session.has_key('lid'):
        # a=request.session['lid']
        if request.method == 'POST':
            fullname =request.POST['fullname']
            email = request.POST['email']
            phone = request.POST['phone']
            company = request.POST['company']
            brand = request.POST['brand']
           
            form5 = Register(fullname=fullname, email=email, phone=phone,company=company,brand=brand)
            form5.save()  
                
            return redirect('login')
        else:
                
            return render(request, 'register.html')
   
def log(request):
    if request.method == 'POST':
        
        email = request.POST['email'] 
        password = request.POST['password']
        user = Register.objects.all().filter(email=email, fullname=password)
        print(user)
        if user:
            for x in user:
                # email1=x.email1
                # password=x.password
                request.session['lid']=x.id
                fullname=x.fullname
                print(fullname)
                request.session['fullname']=fullname

                if email==email and fullname==password :
                    
                    
                    return HttpResponseRedirect('user')
                else:
                    return HttpResponseRedirect('login')
        else:
            messages.error(request, 'invalid Username or Passwords')		
            return HttpResponseRedirect('login')
    else:
        
        return render(request,'login.html')
def user(request):
    if request.session.has_key('lid'):
        b=request.session['lid'] 
        a=request.session['fullname']
        c=request.session['email']
        print(b)
        print(a)
        return render(request, 'user.html',{'b':b,'a':a,'c':c})