from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('cssplayground/', views.css_playground, name="cssplayground"),
    path('jsplayground/', views.js_playground, name="jsplayground")
]