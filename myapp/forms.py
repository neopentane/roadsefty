from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Myuser ,Shedular

class UserRegisterForm(UserCreationForm):
	first_name=forms.CharField(required=True, label="First Name")
	last_name=forms.CharField(required=True, label="Last Name")
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1','password2','first_name','last_name']
	def save(self,commit = True):
		user = super(UserRegisterForm, self).save(commit = False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField(label='Username',required=True)
	password = forms.CharField(widget=forms.PasswordInput(),label="Password",required=True)

class MyUserRegisterForm(forms.ModelForm):
	class Meta:
		model= Myuser
		fields = ['Address','City','Age','PhoneNumber']
		exclude=['user']

class ShedularForm(forms.ModelForm):
	class Meta:
		model = Shedular
		fields = ['url','time']
		labels = {
			"time":"Time (eg : 2020-05-20 12:31)"
		}