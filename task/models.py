from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    country = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    country = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name        

class Tasks(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=20)
    # A Task can have many assignements
    assignments = models.ManyToManyField(Student, related_name="assignments")
    owner = models.CharField(max_length=100)
    created_time = models.DateTimeField(editable=False, auto_now= True)
    modified_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name  


