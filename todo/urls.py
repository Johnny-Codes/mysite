from django.urls import path

from .views import createToDoFormView, deleteToDoFormView
from . import views
from .models import toDo

urlpatterns = [
    path('', views.toDoHomeView, name="todohome"),
    path('delete/<int:pk>', deleteToDoFormView.as_view(model=toDo), name="deletetodo"),
    path('create/', createToDoFormView.as_view(), name="createtodo"),
]