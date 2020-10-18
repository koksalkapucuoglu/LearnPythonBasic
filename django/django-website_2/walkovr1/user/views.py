from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout # django'daki gerekli formlar
from django import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import UserUser

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)#get request olduğunda none tarafı çalışır.
    if form.is_valid():#clean methodunu çağırır böylece alanlarda bir sıkıntı yoksa return ile değerleri döndürür ve form is valid  "true" olur.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            #usera = User.objects.filter(username = username) # user kullanıcısının bilgilerini aldık.
            #print(usera[0].username)
            
            newUser = User(username = username, email = email)
            newUser.set_password(password)
            
            newUser.save()#böylece kullanıcı veri tabanına kayıt olacak
            login(request,newUser)#user'ımız hem kayıt oldu hem de login methodu ile giriş yaptı.
            messages.success(request,"Başarıyla Kayıt Oldunuz...")
            return redirect("index")#walkovr.urls'de anasayfayı tanımlarken name = "index" olarak tanımlamıştık. Böylecek index adını çağırdığımızda anasayfa url'sine gider.
    context = {
        "form": form
    }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context  = {
        "form":form
    }
#burada clean islemi yapmıyoruz ve form fonksiyonu içinde clean nasıl çalışıyorsa aynı şekilde çalışmaya devam edece
    if form.is_valid(): #formda bir sorun var mı yok mu
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username,password=password)#databaseye bakar ve böyle bir veri varsa bunu döner

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render (request,"login.html",context)

        messages.success(request,"Başarıla Giriş Yaptınız...")
        login(request,user)
        serializer = UserSerializer(user, many=True)
        print(serializer)
        return redirect("content:panel")
         
    return render(request,"login.html",context) 
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    
    return redirect("index")

class UserAPI(APIView):
    def get(self, request):
        users = User.objects.filter()
        #content = Content.objects.all()
        serializer = UserSerializer(users, many=True)
        #print(serializer.data[0]["id"])
        return  Response(serializer.data)
    def post(self):
        pass

def login(request):
    form = LoginForm(request.POST or None)

    context  = {
        "form":form
    }
#burada clean islemi yapmıyoruz ve form fonksiyonu içinde clean nasıl çalışıyorsa aynı şekilde çalışmaya devam edece
    if form.is_valid(): #formda bir sorun var mı yok mu
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        u = UserUser.objects.get(username = username)
        print(u)
        if u:
            if password == u.__dict__["password"]:
                messages.success(request,"Başarıla Giriş Yaptınız...")
                    #login(request,user)
                    #serializer = UserSerializer(user, many=True)
                    #print(serializer)
                return render(request,"index.html")
                #return redirect("content:panel")
    else:
        return render(request,"login.html",context) 