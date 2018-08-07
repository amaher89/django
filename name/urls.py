from django.urls import path
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from name.models import name

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', ListView.as_view(queryset=name.objects.all(),template_name="name_list.html")),
    path('add/', views.add, name='add'),
    path('add/add_person_commit.html', views.add_commit, name='add_commit'),
]
