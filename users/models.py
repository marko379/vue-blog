from django.db import models
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from PIL import Image, ImageDraw,ImageOps
# import numpy as np



class User_photo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
	user_img = models.ImageField(default='user_profile_images/brave.jpeg' ,upload_to='user_profile_images/',blank=True, null=True)
	avatar_photo = models.ImageField(default='avatar_images/avatar.png',upload_to='avatar_images/',blank=True, null=True)
	# user_img = models.ImageField(upload_to='user_profile_images/', default='avatar.png' ,blank=True, null=True)
	# avatar_photo = models.ImageField(upload_to='avatar_images/', default='avatar.png',blank=True, null=True)
	# user_img = models.ImageField(default='user_profile_images/brave.jpeg' ,upload_to='user_profile_images/')
	# avatar_photo = models.ImageField(default='avatar_images/avatar.png',upload_to='avatar_images/')

	def save(self,*args, **kwargs):
		super().save(*args, **kwargs)  # saving image first
		if self.user_img:
			img = Image.open(self.user_img.path) # Open user_img using self
			img = ImageOps.exif_transpose(img)
			# if img.width > img.height:
			# 	img = img.rotate(-90,expand=True)


			if img.height > 450 or img.width > 450:
				new_img = (450,445 )
				img.thumbnail(new_img)
				img.save(self.user_img.path)  # saving user_img at the same path

	def image_path(self):
		# return 'http://127.0.0.1:8000' + self.user_img.url
		return 'https://vue-blog-production.up.railway.app' + self.user_img.url

	def image_avatar_path(self):
		# return 'http://127.0.0.1:8000' + self.avatar_photo.url
		return 'https://vue-blog-production.up.railway.app' + self.avatar_photo.url


	def __str__(self):
		if self.user:
			return self.user.username
		else:
			return 'unknown'


	

class MyUserModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def user_profile_photo(self):
		# return 'http://127.0.0.1:8000' + self.user.user_photo.user_img.url
		return 'https://vue-blog-production.up.railway.app' + self.user.user_photo.user_img.url

	def user_profile_username(self):
		return self.user.username

	def user_profile_email(self):
		return self.user.email

	def __str__(self):
		if self.user:
			return 'My user model ' + self.user.username
		else:
			return 'unknown'



class Exe(models.Model):
	img = models.ImageField(upload_to='exe_images/',blank=True, null=True)
	text = models.CharField(max_length=255)

	def __str__(self):
		if self.text:
			return self.text[:10]
		else:
			return 'no text available'



