from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="main"),
    path("post", views.post, name="post"),
    path("aboutme", views.aboutme, name="ffff"),
    path("feedback", views.feedback, name="feedback"),
]