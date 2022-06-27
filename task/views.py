from asyncio import tasks
from email import message
from pydoc import describe
from unicodedata import name
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from typing import Iterator
from django.shortcuts import redirect, render,HttpResponse
from django.db.models import F
import re
from datetime import date
from django.contrib.sessions.models import Session
from django.urls import reverse
from .models import Teacher, Student, Tasks
from django.contrib import messages
from django.template import loader

# Create your views here.

def register_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('emailid')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        password=request.POST.get('password')
        experience = request.POST.get('exp')
        # if name textbox has no data
        if name == "" or name == None:
            context={
                'message': 'Name Field Cannot be Empty'
            }
            return render(request,'teacher_reg.html',context)
        elif email == "" or email == None:
            context={
                'message': 'Email Field cannot be Empty'
            }
            return render(request,'teacher_reg.html',context)
        elif password == "" or password == None:
            context= {
                'message' : 'Password Field Cannot be Empty'
            }
            return render(request,'teacher_reg.html',context)
        elif re.fullmatch(r'^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$',password) == None:
            context= {
                'message' : 'Password must contain minimum 8 characters and atleast 1 Uppercase,Lowercase,Digit and Special Character'
            }
            return render(request,'teacher_reg.html',context)
        elif phone == "" or phone == None or country == "" or country == None or experience == "" or experience == None:
            context= {
                'message' : 'Make sure all the fields are filled!!'
            }
            return render(request,'teacher_reg.html',context)
        else:
            users_email = Teacher.objects.filter(email = email)
            users_phone = Teacher.objects.filter(phone = phone)
            if users_email.count() > 0:
                context = {
                    'message' : 'Username Already Exists'
                }
                return render(request,'teacher_reg.html',context)
            elif users_phone.count() > 0:
                context = {
                    'message' : 'Phone Number Already Exists'
                } 
                return render(request,'teacher_reg.html',context)
            else:
                register = Teacher(name=name,email=email,phone=phone,country=country,password=password,experience=experience)
                register.save()
                messages.success(request, 'Teacher Created')
                return render(request,'loginTeacher.html')
    else:
        context = {}
        return render(request,'teacher_reg.html',context)

def register_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('emailid')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        password=request.POST.get('password')
        gender = request.POST.get('gender')
        if name == "" or name == None:
            context={
                'message': 'Name Field Cannot be Empty'
            }
            return render(request,'stud_register.html',context)
        elif email == "" or email == None:
            context={
                'message': 'Email Field cannot be Empty'
            }
            return render(request,'stud_register.html',context)
        elif password == "" or password == None:
            context= {
                'message' : 'Password Field Cannot be Empty'
            }
            return render(request,'stud_register.html',context)
        elif re.fullmatch(r'^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$',password) == None:
            context= {
                'message' : 'Password must contain minimum 8 characters and atleast 1 Uppercase,Lowercase,Digit and Special Character'
            }
            return render(request,'stud_register.html',context)
        elif phone == "" or phone == None or country == "" or country == None or gender == "" or gender == None:
            context= {
                'message' : 'Make sure all the fields are filled!!'
            }
            return render(request,'stud_register.html',context)
        else:
            users_email = Student.objects.filter(email = email)
            users_phone = Student.objects.filter(phone = phone)

            #if email or mobile number already taken
            if users_email.count() > 0:
                context = {
                    'message' : 'Email Already Exists'
                }
                return render(request,'stud_register.html',context)
            elif users_phone.count() > 0:
                context = {
                    'message' : 'Phone Number Already Exists'
                } 
                return render(request,'stud_register.html',context)
            else:
                register = Student(name=name,email=email,phone=phone,country=country,password=password,gender=gender)
                register.save()
                messages.success(request, 'Student Created')
                return render(request,'login.html')
    else:
        context = {}
        return render(request,'stud_register.html',context)

def login_student(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username == "" or username == None:
            context={
                'message': 'Username Field Cannot be Empty'
            }
            return render(request,'login.html',context)
        elif password == "" or password == None:
            context= {
                'message' : 'Password Field Cannot be Empty'
            }
            return render(request,'login.html',context)
        else:
            if '@' in username:
                kwargs = {
                    'email': username,
                    'password': password

                }
            else:
                kwargs = {'phone': username,'password': password}
            try:
                user = Student.objects.get(**kwargs)
                print(user)
                if user:
                    request.session['username'] = username
                    print(request.session['username'])
                    return redirect('/student')
            except Student.DoesNotExist:
                context = {
                    'message' : 'Wrong Credentials'
                }
                return render(request,'login.html',context)
    return render(request,'login.html')

def login_teacher(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username == "" or username == None:
            context={
                'message': 'Username Field Cannot be Empty'
            }
            return render(request,'loginTeacher.html',context)
        elif password == "" or password == None:
            context= {
                'message' : 'Password Field Cannot be Empty'
            }
            return render(request,'loginTeacher.html',context)
        else:
            # to check whether the username is email or phone number
            if '@' in username:
                kwargs = {
                    'email': username,
                    'password': password

                }
            else:
                kwargs = {'phone': username,'password': password}
            try:
                user = Teacher.objects.get(**kwargs)
                print(user)
                if user:
                    request.session['username'] = username
                    print(request.session['username'])
                    return redirect('/index')
            except Student.DoesNotExist:
                context = {
                    'message' : 'Wrong Credentials'
                }
                return render(request,'loginTeacher.html',context)
    return render(request,'loginTeacher.html')

def index(request):
    # if user is not logged in
    if not request.session.get('username'):
        return redirect('/login_teacher')
    print(request.session.get('username'))
    users_name = Teacher.objects.filter(email=request.session.get('username'))
    a = users_name.values_list()
    owner_task = a[0][0]
    # data = RegisterTeacher.objects.filter(Task__owner = users_name)
    data = Tasks.objects.filter(owner=owner_task)
    for x in data:
        print(x.id)
    # # print(RegisterTeacher.objects.filter(Task__owner = users_name))
    context = {
        'task_data' : data,
    }
    # print(context)
    return render(request,'teacherDashboard.html',context)
    
def task(request):
    std = Student.objects.all().values()
    
    if request.method == 'POST':
        if not request.session.get('username'):
            return redirect('/login')
        name=request.POST.get('name')
        description=request.POST.get('description')
        student_selected = request.POST.getlist("students")
        print("hello")
        print(student_selected)
        if name == "" or description == "" or student_selected == "":
            context = {
                'std': std,
                'message' : 'No Fields should be Empty'
            }
            return render(request,'addTask.html',context)
        else:
            users_name = Teacher.objects.filter(email=request.session.get('username'))
            a = users_name.values_list()
            owner_task = a[0][0]
            newTask = Tasks(name=name, description=description,owner = owner_task, status = 1)
            newTask.save()
            
            students = Student.objects.filter(id__in = student_selected)
            # print(students)
            #For assigned students to task
            for student in students:                
                print(student)
                assignment = student
                assignment.save()
                newTask.assignments.add(assignment)
                newTask.save()
            return redirect('/index')
    
    if request.session['username'] == None:
        return redirect('login')

    context = {
        'std': std
    }
    # print(context)
    return render(request,'addTask.html',context)

def student(request):
    if not request.session.get('username'):
        return redirect('/login_student')
    print(request.session.get('username'))
    users_name = Student.objects.filter(email=request.session.get('username'))
    a = users_name.values_list()
    owner_task = a[0][0]
    print(owner_task)
    
    task = Tasks.objects.filter(assignments = owner_task)
    tasks = task.values_list().values()
    print(tasks)
    context = {
        'tasks': tasks
    }
    return render(request,'student.html',context)

def editTask(request,id):
    std = Student.objects.all().values()
    
    if not request.session.get('username'):
        return redirect('/login')
    on_task = Tasks.objects.get(id = id)
    template = loader.get_template('editTask.html')
    print(on_task.description)
    context = {
        'std': std,
        'task': on_task,
    }
    return HttpResponse(template.render(context, request))


def updateTask(request, id):
    name = request.POST.get('name')
    description = request.POST.get('description')
    status = request.POST.get('status')
    student_selected = request.POST.getlist("students")
    print(student_selected)
    update_task = Tasks.objects.get(id=id)
    update_task.name = name
    update_task.description = description
    update_task.status = status
    update_task.save()

    students = Student.objects.filter(id__in = student_selected)
    print(students)
    for student in students:                
        print(student)
        assignment = student
        assignment.save()
        update_task.assignments.add(assignment)
        update_task.save()
    return HttpResponseRedirect(reverse('index'))

def logout(request):
    if not request.session.get('username'):
        return redirect('/login_teacher')
    Session.objects.all().delete()
    return redirect('/login_teacher')