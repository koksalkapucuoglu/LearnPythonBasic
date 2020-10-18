from django.shortcuts import render, HttpResponse, redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .models import GameStatistic
from .forms import GameStatisticForm   #, AddGroupForm, RemoveGroupForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
