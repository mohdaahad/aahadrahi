from django.contrib import admin

# Register your models here.
from edu.models import student
# from edu.forms import StudentRegistration

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stuemail','stupass')

# @admin.register(StudentRegistration)
# class StudentRegistrationAdmin(admin.ModelAdmin):
#     list_display=('name','email')
    