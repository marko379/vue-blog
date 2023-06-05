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
<<<<<<< HEAD
		# return 'http://127.0.0.1:8000' + self.user_img.url
		return 'https://vue-blog-production.up.railway.app' + self.user_img.url

	def image_avatar_path(self):
		# return 'http://127.0.0.1:8000' + self.avatar_photo.url
=======
		return 'https://vue-blog-production.up.railway.app' + self.user_img.url

	def image_avatar_path(self):
>>>>>>> 0d1f1b3b7aa322bd3b26a2f3abf51896f6da6fb9
		return 'https://vue-blog-production.up.railway.app' + self.avatar_photo.url


	def __str__(self):
		if self.user:
			return self.user.username
		else:
			return 'unknown'


	

class MyUserModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def user_profile_photo(self):
<<<<<<< HEAD
		# return 'http://127.0.0.1:8000' + self.user.user_photo.user_img.url
=======
>>>>>>> 0d1f1b3b7aa322bd3b26a2f3abf51896f6da6fb9
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






######### PICTURE DRAWING ##############################

# class User_photo(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	user_img = models.ImageField(upload_to='user_profile_images/',blank=True, null=True)
# 	thumbnail = models.ImageField(upload_to='thumbnail_images/',blank=True, null=True)

# 	def save(self,*args, **kwargs):
# 		super().save(*args, **kwargs)  # saving image first
# 		if self.user_img:
# 		# (1920, 863) ppppppppppppppp  ( (x1 + x2) / 2, (y1 + y2) / 2 ) // [(x0, y0),(x1, y1)] or [x0, y0, x1, y1]
# 			# im=Image.open(self.user_img.path)
# 			# print(im.size,'ppppppppppppppp')
# 			# draw = ImageDraw.Draw(im)
# 			# # draw.ellipse((80,80,200,200), fill = 'yellow', outline ='blue')
# 			# draw.ellipse((180,180,400,400), fill = 'yellow', outline ='blue')
# 			# # draw.line((0, im.size[1], im.size[0], 0), fill=128)
# 			# im.save(self.user_img.path)

# 			# DRAW ELLIPSE
# 			img=Image.open(self.user_img.path)
# 			new_img = (140,135 )
# 			img.thumbnail(new_img)
# 			img = img.rotate(-270,expand=True)
# 			draw = ImageDraw.Draw(img)
# 			draw.line((100,0,100,500),  fill = 'yellow',width=7)
# 			# cropped_img = img.crop((0, 0, 500, 500))
# 			# draw = ImageDraw.Draw(im)
# 			# draw.ellipse((100,600,200,700),  fill = 'red',width=10)
# 			img.save(self.user_img.path)


			# DRAW RECTANGLE
			# im=Image.open(self.user_img.path)
			# draw = ImageDraw.Draw(im)
			# draw.rectangle((100,600,200,700),  fill = 'red',width=10)
			# im.save(self.user_img.path)

			# DRAW LINE
			# im=Image.open(self.user_img.path)
			# draw = ImageDraw.Draw(im)
			# draw.line((100,200,1800,400),  fill = 'red',width=10)
			# # draw.line((500,100,500,100),  fill = 'yellow',width=7)
			# # draw.line((0, im.size[1], im.size[0], 0), fill=128)
			# im.save(self.user_img.path)

			# CROP PICTURE
			# img=Image.open(self.user_img.path)
			# print(img.mode)
			# cropped_img = img.crop((0, 0, 500, 500))
			# cropped_img.save(self.user_img.path)

			# img.save(self.user_img.path)



# 	def image_path(self):
# 		return 'http://127.0.0.1:8000' + self.user_img.url


# 	def __str__(self):
# 		if self.user:
# 			return self.user.username
# 		else:
# 			return 'unknown'



# class NewUser(AbstractUser):
#     new_name = models.CharField(max_length=255)
#     new_email = models.CharField(max_length=255, unique=True)
#     new_password = models.CharField(max_length=255)
#     new_username = None

#     NEW_USERNAME_FIELD = 'email'
#     NEW_REQUIRED_FIELDS = []
