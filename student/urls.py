from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('register/',student_register, name="register"),
    path('login/',student_login, name="login"),
    path('student_board/',student_board, name="studnet_board"),
    path('teacher_board/',teacher_board, name="teacher_board"),
    path('teacher_login/',teacher_login, name="teacher_login"),
    # path('add/',add, name='add'),
    path('result/',result, name='result'),
    path('add/',add, name='add'),
    path('add_result/<int:id>',add_result, name='add_result'),
    path('show_result/',show_result, name='show_result'),
    path('approve/',approve, name='approve'),
    path('accept/<int:id>',accept, name='accept'),
    path('update/',update, name='update'),
    # path("teacher_register/",teacher_register, name="teacher_register"),
    # path('teacher_add/',teacher_add, name='teacher_add'),
    # path('delete/<int:id>',delete, name='delete'),
]