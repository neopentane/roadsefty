from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Myuser,Shedular
from .forms import UserRegisterForm,MyUserRegisterForm,LoginForm,ShedularForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		form2=MyUserRegisterForm(request.POST)
		if form.is_valid() and form2.is_valid():
			new_user=form.save()
			new_myuser=form2.save(commit=False)
			new_myuser.user=new_user
			new_myuser.save()
			messages.add_message(request, messages.SUCCESS, 'Created User Successfully!')
			return redirect('login')
	else:
			form = UserRegisterForm()
			form2=MyUserRegisterForm()
	return render(request, 'myapp/index.html', {'form': form,'form2':form2})

def userlogin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user is not None :
				login(request,user)
				return redirect('home')
			else:
				messages.add_message(request, messages.WARNING, 'Username and password didnot matched!')
	else :
		form = LoginForm()
	return render(request,'myapp/login.html',{'form':form})

@login_required(login_url='/login')
def home(request):
	messages.add_message(request, messages.INFO, 'Loged in')
	myuser=Myuser.objects.get(user=request.user)
	return render(request,'myapp/home.html',{"myuser":myuser})

def userlogout(request):
	messages.add_message(request, messages.INFO, 'logged out!')
	logout(request)
	return redirect('signup')

def scheduler(request):
	if request.method == "POST":
		form = ShedularForm(request.POST)
		if form.is_valid():
			form.save()
	else :
		form = ShedularForm()
	return render(request,'myapp/scheduler.html',{'form':form})