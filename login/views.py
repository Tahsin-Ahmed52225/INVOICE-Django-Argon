from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from passlib.hash import pbkdf2_sha256
from .models import account
@csrf_exempt
def index(request):
    if ( request.method == "POST"):
        #Finding the username
        user = request.POST["username"]
        if account.objects.filter(email= user):
            user_obj = account.objects.get(email= user)
            if user_obj.verify_password(request.POST["password"]):
               return render(request,'dashboard.html')
        else:
            print("Wrong password")
            return render(request, 'index.html')



    return render(request, 'index.html')
@csrf_exempt
def register(request):
    if ( request.method == "POST"):
        account.objects.create(name= request.POST["name"],
                               email=request.POST["email"],
                               phone=request.POST["phone"],
                               job=request.POST["job"],
                               # Saving the password after encrypting
                               passwd= pbkdf2_sha256.encrypt(request.POST["passwd"],rounds = 12000 , salt_size = 32))
        return redirect('index')
    else :
        return render(request, 'register.html')


