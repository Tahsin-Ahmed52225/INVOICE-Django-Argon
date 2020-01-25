from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from passlib.hash import pbkdf2_sha256
from .models import account
@csrf_exempt
def index(request):
    if ( request.method == "POST"):
        log = account.objects.filter(email=request.POST["username"],passwd = request.POST["password"])
        if log:
            return render(request,'dashboard.html')
        else:
            return render(request, 'index.html')


    return render(request, 'index.html')
@csrf_exempt
def register(request):
    if ( request.method == "POST"):
        account.objects.create(name= request.POST["name"],email=request.POST["email"], phone=request.POST["phone"],job=request.POST["job"],passwd= pbkdf2_sha256.encrypt(request.POST["passwd"],rounds = 12000 , salt_size = 32))
        return redirect('index')
    else :
        return render(request, 'register.html')


