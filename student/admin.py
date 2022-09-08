from django.contrib import admin
from student.models import Student, Teacher, User,Result
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class TeacherAdmin(UserAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)

# class StudentAdmin(UserAdmin):
#     pass
# admin.site.register(Student,StudentAdmin)


admin.site.register(User)
admin.site.register(Result)
admin.site.register(Student)