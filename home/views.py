from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request,'index.html')

def loginuser(request):
    if request.method ==  "POST":
        email = request.POST.get('email')
        pass2 = request.POST.get('pass2')
        user = authenticate(username=email,password=pass2)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            print("noooooooooooooooooo")
    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return render(request,'index.html')
def signupuser(request):
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
        return render(request,'signup.html')