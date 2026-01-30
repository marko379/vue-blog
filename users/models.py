from django.db import models
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from PIL import Image, ImageDraw,ImageOps
import cloudinary
from cloudinary.models import CloudinaryField
import cloudinary.uploader
import cloudinary.api	



class User_photo(models.Model):
	
	user  = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)

	user_img = CloudinaryField(
		'user_profile',
		folder='media/user_profile_images',
		transformation={'width': 450, 'height': 450, 'crop': 'limit', 'quality': 'auto'},
		blank=True,
		null=True
	)	
	avatar_photo = CloudinaryField('avatar',folder='media/avatar_images', blank=True, null=True)


	def image_path(self):
		if self.user_img and self.user_img.url:
			return self.user_img.url
		else:
			# return '/static/10.jpg'   # make sure this file exists!
			return self.avatar_photo.url  # make sure this file exists!


	def image_avatar_path(self):
		if self.avatar_photo and self.avatar_photo.url:
			return self.avatar_photo.url
		else:
			return '/static/10.jpg'    # your default avatar


	def change_users_photo(self):
		print(self.user_img)


	


	def __str__(self):
		if self.user:
			return self.user.username
		else:
			return 'unknown'



	

class MyUserModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def user_profile_photo(self):
		self.user_img.url
		# return 'http://127.0.0.1:8000' + self.user.user_photo.user_img.url
		# return 'https://vue-blog-production.up.railway.app' + self.user.user_photo.user_img.url

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

