from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def first(request): 
    return render(request,'1.html')
def second(request):
    return render(request,'2.html')    
def doctors(request): 
    return render(request,'doctors.html')
def help(request): 
    return render(request,'help.html')
def hospitals(request): 
    return render(request,'hospitals.html')
def registerform(request): 
    return render(request,'registerform.html')
def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('second')
    else:
        return HttpResponse('error 404 - not found')  
        
def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('second')
        else:
            return HttpResponse('<h1>Wrong Credentials ,If You Forget Your Password Then You Can Create Your Account Again With Same Email ID But Book The Appointment Through The Email Which You Currently Use So You Can Easily Get The Payment Link</h1>') 
    else:
        return HttpResponse('error 404- not found')     
              
def handlelogout(request):
    logout(request)       
    return redirect('first')     







