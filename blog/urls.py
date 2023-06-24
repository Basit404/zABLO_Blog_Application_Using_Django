from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path("blog/", views.blog, name = "blog"),
    path("blogpost/<str:slug>", views.blogpost, name = "blogpost"),
    path("feedback/", views.feedback, name = "feedback"),
    path("about/", views.about, name = "about"),
]