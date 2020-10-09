from django.urls import path
from app import views as app_views

urlpatterns = [
    path('', app_views.home, name="home"),
    path('view/<int:pk>', app_views.todo_display, name="todo-view"),
    path('update/<int:pk>', app_views.todo_update, name="todo-update"),
    path('create', app_views.todo_create, name="todo-create"),
    path('delete/<int:pk>', app_views.todo_delete, name="todo-delete"),
]


