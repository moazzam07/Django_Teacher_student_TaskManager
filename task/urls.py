from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path("register_teacher", views.register_teacher, name = 'register_teacher'),
    path("register_student", views.register_student, name = 'register_student'),
    path("login_student", views.login_student, name = 'login_student'),
    path("login_teacher", views.login_teacher, name = 'login_teacher'),
    path("index", views.index, name = 'index'),
    path("task", views.task, name = 'task'),
    path('logout',views.logout,name="logout"),
    path("student", views.student, name = 'student'),
    path('editTask/<int:id>', views.editTask, name = 'editTask'),
    path('editTask/updateTask/<int:id>', views.updateTask, name = 'updateTask')
]