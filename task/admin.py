from django.contrib import admin
from task.models import Teacher, Student, Tasks

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Tasks)