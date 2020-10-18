from django.shortcuts import render, HttpResponse, redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .models import Content
from .forms import ContentForm, AddGroupForm, RemoveGroupForm
from gamestatistic.forms import GameStatisticForm
from gamestatistic.models import GameStatistic
from django.contrib import messages
from django.contrib.auth.models import Group, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContentSerializer
# Create your views here.

def index(request):
    return render(request,"index.html") #template dönmek için bu şekilde bir return yazarız.
    #return HttpResponse("<h3>HOME</h3>")#bu fonksiyonla http response dönebiliriz

@login_required(login_url = "user:login")
def panel(request):
    my_groups_q= request.user.groups.all()
    my_groups = list(my_groups_q)
    if len(my_groups) >= 2:
        
        for i in range(len(my_groups)):
            group = Group.objects.get(name = my_groups[i].name)
            users_q = group.user_set.all()
            users = list(users_q)
            users.remove(request.user)
            contents = Content.objects.filter(user__in = users )
            context = {
            "contents":contents
            }
            return render(request,"commercialpanel.html",context)
            
    elif request.user.username == "walkovradmin" :
        contents = Content.objects.filter
        context = {
        "contents":contents
        }
        return render(request,"adminpanel.html",context)
    else:
        contents = Content.objects.filter(user = request.user)
        gamestatistics = GameStatistic.objects.filter(user = request.user)
        #contents = Content.objects.filter() # user kullanıcısının bilgilerini aldık. 
        context = {
            "contents":contents,
            "gamestatistics": gamestatistics
        }
        return render(request,"panel.html",context) 

@login_required(login_url = "user:login")
def addContent(request):
    form = ContentForm(request.POST or None)

    if form.is_valid():
        content = form.save(commit="False")#buradaki bilgilere göre, biz modelle ilişkili bir hale getirdiğimiz için veritabanında otomatik olarak olusacak.
        #burada save işlemini yapma, biz kendimiz yapacağız bu işlemi
        content.user = request.user
        content.save()

        messages.success(request,"Statistic has been successfully added")
        return redirect("content:panel")


    return render(request,"addcontent.html",{"form":form})

@login_required(login_url = "user:login")
def adminpanel(request): 
    if request.user.username == "walkovradmin" :
        contents = Content.objects.filter
        context = {
        "contents":contents
        }
        return render(request,"adminpanel.html",context) 
    else:
        messages.info(request,"admin login required")
        
        return render(request,"index.html")

def userdetail_atadmin(request,id): #django otomatik olarak bu id'yi gönderir. çünkü url.py'de id değiskeni ile aldık.
    #print("id:" +  str(id))
    if request.user.username == "walkovradmin" :
        contents = Content.objects.filter(user_id = id)
        gamestatistics = GameStatistic.objects.filter(user_id = id)
        context = {
                "contents":contents,
                "gamestatistics": gamestatistics
        }
        return render(request,"userdetail.html",context)
    else:
        messages.info(request,"admin login required")
        
        return render(request,"index.html")
    #content = Content.objects.get(user_id = id)
    """for content in contents:
        print(content.user)
        print(content.user_id)
        print(content.session_count)"""  
    

def userdetail_atcommercial(request,id): #django otomatik olarak bu id'yi gönderir. çünkü url.py'de id değiskeni ile aldık.
    #print("id:" +  str(id))
    my_groups_q= request.user.groups.all()
    my_groups = list(my_groups_q)
    if len(my_groups) >= 2:
        contents = Content.objects.filter(user_id = id)
        gamestatistics = GameStatistic.objects.filter(user_id = id)
        context = {
            "contents":contents,
            "gamestatistics": gamestatistics
        }
        return render(request,"userdetail.html",context)
    else:
        messages.info(request,"commercial login required")
        
        return render(request,"index.html")
    #content = Content.objects.get(user_id = id)
    """for content in contents:
        print(content.user)
        print(content.user_id)
        print(content.session_count)"""
    

@login_required(login_url = "user:login")
def addtoGroup(request):
    form = AddGroupForm(request.POST or None)
    #kullanıcının dahil oldugu grubu getirme
    my_groups_q= request.user.groups.all()
    my_groups = list(my_groups_q)
    my_group_name = my_groups[0]
    
    if form.is_valid():
        username = form.cleaned_data.get("username")

        user_q = User.objects.filter(username = username)
        user = list(user_q)

        user_id = user[0].id
        #kullanıcının dahil olduğu gruba yeni bir kullanıcı ekleme(id ile)
        my_group = Group.objects.get(name=my_group_name) 
        my_group.user_set.add(user_id)
        
        messages.success(request,"User has been successfully added")
        return redirect("content:panel")

    return render(request,"addtogroup.html",{"form":form})

@login_required(login_url = "user:login")
def removefromGroup(request):
    form = RemoveGroupForm(request.POST or None)
    #kullanıcının dahil oldugu grubu getirme
    my_groups_q= request.user.groups.all()
    my_groups = list(my_groups_q)
    my_group_name = my_groups[0]
    
    if form.is_valid():
        username = form.cleaned_data.get("username")

        user_q = User.objects.filter(username = username)
        user = list(user_q)

        user_id = user[0].id
        #kullanıcının dahil olduğu gruba yeni bir kullanıcı ekleme(id ile)
        my_group = Group.objects.get(name=my_group_name) 
        my_group.user_set.remove(user_id)
        
        messages.success(request,"User has been successfully removed")
        return redirect("content:panel")

    return render(request,"removefromgroup.html",{"form":form})

class ContentAPI(APIView):
    def get(self, request):
        contents = Content.objects.filter(user = request.user)
        gamestatistics = GameStatistic.objects.filter(user = request.user)
        #content = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        print(serializer.data[0]["id"])
        print(serializer.data[0]["session_count"])
        print(serializer.data[0]["total_step"])
        print(serializer.data[0]["total_walk"])
        return  Response(serializer.data)
    def post(self):
        pass