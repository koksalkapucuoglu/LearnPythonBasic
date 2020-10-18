from django.shortcuts import render,redirect
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)#get request olduğunda none tarafı çalışır.
    if form.is_valid():#clean methodunu çağırır böylece alanlarda bir sıkıntı yoksa return ile değerleri döndürür ve form is valid  "true" olur.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            
            newUser.save()#böylece kullanıcı veri tabanına kayıt olacak
            login(request,newUser)#user'ımız hem kayıt oldu hem de login methodu ile giriş yaptı.
            messages.warning(request,"Başarıyla Kayıt Oldunuz...")
            return redirect("index")#blog.urls'de anasayfayı tanımlarken name = "index" olarak tanımlamıştık. Böylecek index adını çağırdığımızda anasayfa url'sine gider.
    context = {
        "form": form
    }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context  = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username,password=password)#databaseye bakar ve böyle bir veri varsa bunu döner

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render (request,"login.html",context)

        messages.success(request,"Başarıla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
         
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    
    return redirect("index")
