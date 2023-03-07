from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from .models import User_photo



		
class Create_User(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']


class User_photo_form(forms.ModelForm):
	class Meta:
		model = User_photo
		fields = ['user_img','avatar_photo']