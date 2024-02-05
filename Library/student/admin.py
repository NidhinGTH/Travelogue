from django.contrib import admin

# Register your models here.
from student.models import student
from student.models import  CustomUser
admin.site.register(student)
admin.site.register(CustomUser)