from django.shortcuts import render ,redirect
from django.http  import HttpResponse
from .models import Captain
from .forms import CaptainForm , UserRegistrationForm , LoginForm
from django.contrib.auth import authenticate , login


# Create your views here.
def user_login(request):
	form =LoginForm()
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():   #request.method =="POST":
			x =form.cleaned_data['username']
			y =form.cleaned_data['password']

			auth_user = authenticate(username=x ,password=y)
			if auth_user is not None:
				login(request,auth_user)
				return redirect("hulk_hulk")
	context ={
		"form":form
	}
						
	return render(request, 'login.html', context)
def user_registration(request):
	form =UserRegistrationForm()
	if request.method =="POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():   #request.method =="POST":
			user =form.save(commit=False)
			user.set_password(user.password)
			user.save()
			return redirect("hulk_hulk")
	context ={
		"form":form
	}
	return render(request, 'register.html', context)




def ironman(request):
 	avengers =Captain.objects.all().order_by('name')
 	query = request.GET.get('q')
 	
 	if query:
 		avengers=avengers.filter(name__contains=query) #double underscore 

 	context ={
 		"avengers" :avengers

 	}

 	return render(request, "list_view.html", context)

def detail(request,fury_id): 
 	context ={
 		"avengers" : Captain.objects.get(id=fury_id),


 	}
 	return render(request,"detail.html", context)

def create(request):
	form = CaptainForm()
	if request.method =="POST" :
			form =CaptainForm(request.POST, request.FILES or None)
			if form.is_valid():
				form.save()
				return redirect("hulk_hulk")
	context ={
		'form' :form,
	}
	return render(request,'create.html',context)

def update(request, fury_id):
	game= Captain.objects.get(id=fury_id)
	form = CaptainForm(instance=game)
	if request.method =="POST" :
			form =CaptainForm(request.POST, instance= game)
			if form.is_valid():
				form.save()
				return redirect("hulk_hulk")
	context ={
		'game' :game,
		'form':form,
	}
	return render(request,'update.html', context)

def delete(request, fury_id) :
	Captain.objects.get(id=fury_id).delete()
	return redirect("hulk_hulk")
	#name_detail is in the urls.py which will redirect the process to an html file 
