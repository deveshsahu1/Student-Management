from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import is_valid_path
from .forms import ResultForm, StudentForm,TeacherForm
from django.contrib.auth import login,authenticate
from .models import Result, Student,Teacher
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def home(request):
	# details = Student.objects.all()
	# context = {'details':details}
	return render(request,'student/home.html')


# Teacher ---------------------------------------------------------------------------------------
@csrf_exempt
def teacher_register(request):
	if request.method == "POST":
		form = TeacherForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = TeacherForm()
	return render (request, "student/teacher_register.html", {"form":form})

@csrf_exempt
def teacher_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			#messages.info(request, f"You are now logged in as {username}.")
			return redirect("teacher_board")
		else:
			return HttpResponse(" Teacher  Invalid id & pwd")

			#messages.error(request,"Invalid username or password.")
	else:
		return render(request,"student/teacher_login.html")

@csrf_exempt
def teacher_board(request):
	return render(request,'student/teacher_board.html')




# Register Student ----------------------------------------------------------
@csrf_exempt
def student_register(request):
	# teacher = Teacher.objects.all()
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = StudentForm()
	return render (request, "student/register.html", {"form":form})


@csrf_exempt
def student_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		student = Student.objects.get(username = username)
		if user is not None:
			if student.is_approve == True:
				login(request, user)
				#messages.info(request, f"You are now logged in as {username}.")
				return redirect("studnet_board")
		else:
			return HttpResponse("1.Student Invalid id & pwd")
			#messages.error(request,"Invalid username or password.")
		return HttpResponse("Teacher is not approve you.....")
		
	else:
		return render(request,"student/login.html")
 

@csrf_exempt
def approve(request):
	user =  request.user.id
	teacher = Teacher.objects.get(id = user)
	student =  Student.objects.filter(teacher_name = teacher , is_approve =False)
	return render(request,'student/request.html',{'student': student})

@csrf_exempt
def accept(request,id):
	student = Student.objects.get(id = id)
	student.is_approve = True 
	student.save()
	return redirect('/teacher_board/')
	


# Show Student data in table ----------------------------------------------------------------------- 
# def add(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         email = request.POST.get("email")
#         username = request.POST.get("username")
#         phone_number = request.POST.get("phone_number")
#         address = request.POST.get("address")
#         school_name = request.POST.get("school_name")
		
#         obj=Student(first_name=first_name,last_name=last_name,username=username,email=email,
#                     phone_number=phone_number,address=address,school_name=school_name)
#         obj.save()
#         return redirect('/')
#     else:
#         return render(request,'student/add.html/')  

@csrf_exempt
def update(request,id):
	if request.method == 'POST':
		user_obj = Student.objects.get(pk=id)
		form = StudentForm(request.POST, instance=user_obj)
		if form.is_valid():
			form.save()
	else:
		user_obj = Student.objects.get(pk=id)
		form = StudentForm(instance=user_obj)
	return render(request, 'student/update.html',{'form':form})


# Result ----------------------------------------------------------------------
@csrf_exempt
def result(request):
	# breakpoint()
	user = Student.objects.all()
	return render(request, 'student/result.html',{'user':user})
		
	# user = Student.objects.first()
	# student = Student.objects.get()
	# result =  result.objects.filter(first_name = student , is_approve =False)
	# return render(request,'student/result.html',{'result': result})

@csrf_exempt
def add(request):
	# breakpoint()
	form =  ResultForm()
	if request.method == "POST":
		form = ResultForm(request.POST)
		if form.is_valid:
			form.save()
	return render(request,'student/teacher_board.html/')

@csrf_exempt
def add_result(request,id):
	# breakpoint()
	# data = get_object_or_404(Student, id=id)
	data = Student.objects.get(id=id)
	form = ResultForm()
	if request.method == "POST":
		form = ResultForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'student/add_result.html', {'form': form, 'data':data})

@csrf_exempt
def show_result(request):
	user = Result.objects.all()
	return render(request,'student/show_result.html',{'user':user})
	
	
@csrf_exempt
def student_board(request):
	return render(request,'student/student_board.html')





# def admin_team_detail(request):
# 	obj= Student.objects.all()
# 	print(request.method)
# 	if request.method == 'POST':
# 		if 'reject' in request.POST :
# 			Student.status = 'reject'
# 		else:
# 			Student.status = 'accept'
# 			Student.save()
# 	return render(request, "", {"object": obj})