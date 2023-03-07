from django import forms
from django.contrib.auth.models import User
# from .models import User_photo
from .models import Comments




class Comment_form(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['article','title','comment','user']