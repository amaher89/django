from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import name
from django import template
import re
from django.template import RequestContext

def index(request):
    return render(request,"base_generic.html")

def list(request):
    return HttpResponse("Hello, world. You're at the polls list.")

def add(request):
    request.session.modified = True
    return render(request,"add_person.html")

def add_commit(request):
    _name = request.POST["name"]
    _mail = request.POST["mail"]
    pattern = re.compile("^(\d|\w|_|\.|\-)+@(\d|\w|\-)+\.\w{2,3}$")
    ready_to_save=True
    if _name == "" :
     messages.warning(request,'Please enter name.')
     ready_to_save=False
    if not pattern.match(_mail):
     messages.warning(request,'Please enter a valid e-mail')
     ready_to_save=False
    objname = name(name= _name,mail= _mail)
    if ready_to_save:
     objname.save()
    request.session.modified = True
    return render(request,"add_person.html")

#    return HttpResponse("Hello, world. You're at the polls add.")
# Create your views here.
