import email
from django import forms
from .models import Result, Student,Teacher
from django.contrib.auth.forms import UserCreationForm
    
# def validate_username(self):
#     self.field['username'].help_text = None
#     self.field['username'].default_validators = []
#     self.field['username'].validators = []



class StudentForm(UserCreationForm):
    # username = forms.CharField(max_length=70,validators=[validate_username])
    username = forms.CharField(help_text=None)
    password1 = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = Student   
        # fields = '__all__'
        # fields = ['username','email','teacher_name']
        # fields = ['username','first_name','last_name','email_id','phone_number',
        # 'address','school_name','teacher_name']
        fields = ['username','first_name','last_name','phone_number',
        'address','school_name','teacher_name']



class TeacherForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Teacher
        fields = ['username','password']



class ResultForm(forms.ModelForm):
    # first_name= forms.FileField(required=False)
    class Meta:
        model=  Result
        fields = '__all__'