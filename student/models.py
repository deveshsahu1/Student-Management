from django.db import models
from django.contrib.auth.models import AbstractUser
# from datetime import datetime
# from django.contrib.auth.models import User 


# class stu(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE())
    
class User(AbstractUser):
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name 
    
    class  Meta:
        abstract = False
    
    
# Teacher Model :--------------------------------------------------------

class Teacher(User):
    t_number = models.CharField(max_length=14)
    t_address = models.CharField(max_length=100)
  
    def __str__(self):
        return self.first_name 
    class  Meta:
        db_table = 'teachers'
        managed = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teacher'
      

# Student Modle :-------------------------------------------------------
# TEACHER_CHOICES = (
#     ('green','GREEN'),
#     ('blue', 'BLUE'),
#     ('red','RED'),
#     ('orange','ORANGE'),
#     ('black','BLACK'),
# )
class Student(User):
    is_approve = models.BooleanField(default=False)
    # email_id = models.CharField(max_length=100,unique=True)s
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=100)
    school_name = models.CharField(max_length=70)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # teacher_name = models.CharField(max_length=6, choices=TEACHER_CHOICES, default='green')
    
    def __str__(self):
        return self.first_name
    class  Meta:
        db_table = 'students'
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        
        
        
class Result(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,blank=True,null=True)
    # name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    hindi = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    total = models.IntegerField()
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    

    # def __str__(self):
    #     return self.student