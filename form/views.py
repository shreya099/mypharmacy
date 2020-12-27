from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "invalid username/password")
            print("ok")
            return redirect("login")
    else:
        return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken!")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already exists!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name)
                user.save()
                return redirect("/")
        else:
            messages.info(request, "password not equal")
            return redirect('register')

        return redirect('index')


    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def cont(request):
    return render(request,'cont.html')