from django.db import models
from django.utils.text import slugify
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.conf import settings



class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(blank=True, null=True)

	def __str__(self):
		return self.name

	def save(self):
		self.slug = slugify(self.name)
		super().save()



class Article(models.Model):
	# category = models.ForeignKey(Category, related_name='article', on_delete=models.CASCADE)
	writer = models.CharField(max_length=70,null=True)
	category = models.ManyToManyField(Category,blank=True,related_name='book_category')
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='article_images/',blank=True, null=True) # upload_to='uploads/',
	date_added = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    
	def __str__(self):
		return self.name

	# you can accsess methods in views and vue template
	# 'http://127.0.0.1:8000' = django server,basiclly go there and get photo
	def image_path(self):
	# Check if the article actually has an image
		if self.image:                                   # ← if there IS an image
			return self.image.url                        # ← this is already the full https://res.cloudinary.com/... URL
		else:                                            # ← if there is NO image
			return '/static/img/default-book.jpg'        # ← fallback picture (put one in static/img/)

	def description_1st_part(self):
		if len(self.description) > 410:
			return self.description[:410]

	def description_2nd_part(self):
		if len(self.description) > 410:
			return self.description[410:]

	def num_of_comments(self):
		comments = Comments.objects.filter(article__slug=self.slug).count()
		return comments

	def categories(self):
		return self.category.all().values_list('name', flat=True)
		

	def save(self):
		self.slug = slugify(self.name)
		super().save()


class Books_in_Basket(models.Model):
	basket = models.ForeignKey(Article,on_delete=models.CASCADE,blank=True,null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
	def __str__(self):
		return 'basket of user- ' + self.user.username

	def book(self):
		return self.basket.name

	def book_price(self):
		return self.basket.price

	def slug(self):
		return self.basket.slug

	def image_path(self):
		# return 'http://127.0.0.1:8000' + self.basket.image.url
		# return 'https://vue-blog-production.up.railway.app' + self.basket.image.url
		return self.image.url if self.image else '/static/img/no-image.jpg'




class Comments(models.Model):
	article = models.ForeignKey(Article,related_name='tracks', on_delete=models.CASCADE,null=True,blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	title = models.CharField(max_length=75)
	comment = models.TextField(blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	comment_likes = models.ManyToManyField(User,related_name='comment_likes',blank=True)
	comment_dislikes = models.ManyToManyField(User,related_name='comment_dislikes',blank=True)

    
	def __str__(self):
		if self.user:
			return 'Article: ' + self.article.name + '------Title: ' + self.title + '------Commented by ' + self.user.username
		return 'Article: ' + self.article.name + '------Title: ' + self.title + '------Commented by ' + 'unknown'

	def username(self):
		if self.user:
			return self.user.username
		return 'anonymous user'

	def userID(self):
		if self.user:
			return self.user.id

	def user_photo(self):
		if self.user:
			return self.user.user_photo.user_img.url
		else:
			print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
			return 'https://vue-blog-production.up.railway.app' + settings.MEDIA_URL  + 'avatar.png'

	def datepublished(self):
		return self.date_added.strftime('%c')

	def user_stars(self):
		if self.user:
			try:
				user_star = Users_stars.objects.get(user_id = self.user.id, article_id=self.article.id).stars
			except:
				user_star = 0
			return user_star

	def user_like_comment_count(self):
		return self.comment_likes.count()

	def user_dislike_comment_count(self):
		return self.comment_dislikes.count()

	def user_like_comment(self):
		return self.comment_likes.all().values_list('id', flat=True)

	def user_dislike_comment(self):
		return self.comment_dislikes.all().values_list('id', flat=True)

	def comment_1st_part(self):
		if len(self.comment) > 300:
			return self.comment[:300]
		else:
			return self.comment

	def comment_2nd_part(self):
		if len(self.comment) > 300:
			return self.comment[300:]



class Rating_star_system(models.Model):
	star = models.OneToOneField(Article,on_delete=models.CASCADE,null=True,blank=True)
	star_1 = models.ManyToManyField(User,blank=True,related_name='star_1')
	star_2 = models.ManyToManyField(User,blank=True,related_name='star_2')
	star_3 = models.ManyToManyField(User,blank=True,related_name='star_3')
	star_4 = models.ManyToManyField(User,blank=True,related_name='star_4')
	star_5 = models.ManyToManyField(User,blank=True,related_name='star_5')

	def __str__(self):
		return self.star.name


	# @property
	def total(self):
		add_all_users = self.star_1.count() + self.star_2.count() + self.star_3.count() + self.star_4.count() +self.star_5.count()
		multiplie_users = self.star_5.count() * 5 + self.star_4.count() * 4 + self.star_3.count() * 3 + self.star_2.count() * 2 + self.star_1.count() * 1

		if multiplie_users > 0 and add_all_users > 0:
			total_rating = multiplie_users/add_all_users
		else:
			total_rating = 0.0
		return round(total_rating,1) , add_all_users

	# @property
	def each_star_procentage(self):
		add_all_users = self.star_1.count() + self.star_2.count() + self.star_3.count() + self.star_4.count() +self.star_5.count()

		if add_all_users != 0:
			star_1 = (self.star_1.count() / add_all_users) * 100
			star_2 = (self.star_2.count() / add_all_users) * 100	
			star_3 = (self.star_3.count() / add_all_users) * 100	
			star_4 = (self.star_4.count() / add_all_users) * 100	
			star_5 = (self.star_5.count() / add_all_users) * 100			
			return round(star_1),round(star_2),round(star_3), round(star_4), round(star_5)
		else:
			star_1 = 0
			star_2 = 0	
			star_3 = 0	
			star_4 = 0	
			star_5 = 0
			return star_1,star_2,star_3,star_4,star_5




class Users_stars(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	stars = models.SmallIntegerField(null=True,blank=True)
	article = models.ForeignKey(Article,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		if not self.user:
			return "{} //// user: ".format(self.article.name)
		return "Article: {}-------------USER: {}-------------STARS-GIVEN: {}".format(self.article.name,self.user.username,self.stars)

	def korisnikova_ocjena(self):
		return self.stars