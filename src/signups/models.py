from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank= True)
	last_name = models.CharField(max_length=120, null=True, blank= True)
	email = models.EmailField()

	timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)
	updated =models.DateTimeField(auto_now_add=False, auto_now=True)
	"""docstring for Signup"""
	
	def __unicode__(self):
		return smart_unicode(self.first_name+'  '+self.last_name)


class Customer(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank= True)
	last_name = models.CharField(max_length=120, null=True, blank= True)
	email = models.EmailField()
	phone = models.IntegerField()
	timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)
	updated =models.DateTimeField(auto_now_add=False, auto_now=True)
	"""docstring for Signup"""
	
	def __unicode__(self):
		return smart_unicode(self.first_name+'  '+self.last_name)



class Person(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank= True)
	last_name = models.CharField(max_length=120, null=True, blank= True)
	email = models.EmailField()
	phone = models.IntegerField()
	timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)
	updated =models.DateTimeField(auto_now_add=False, auto_now=True)
	short_bio = models.CharField(max_length=300, null=True, blank=True)
	# gender = models. 	
	# photo = models.ImageField				


	"""docstring for Signup"""
	
	def __unicode__(self):
		return smart_unicode(self.first_name)


class Article(models.Model):
	article_name = models.CharField(max_length=120, null=True, blank= True)
	short_description = models.CharField(max_length=120, null=True, blank= True)
	article_complete = models.CharField(max_length=1000)
	timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)
	updated =models.DateTimeField(auto_now_add=False, auto_now=True)
	location = models.ManytoManyField(Location)
	# article_type = models.CharField
	# user = models.foreignkey

	def __unicode__(self):
		return smart_unicode(self.article_name)

class Location(models.Model):
	location_name= models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	location_type = models.CharField(max_length=50)
	location_description = models.CharField(max_length=500)
			
	def __unicode__(self):
		return smart_unicode(self.location_name)

class Photo(models.Model):
	# image = models.ImageField()
	# article = models.foreignkey

	def __unicode__(self):
		return smart_unicode(self.image)



class Video(models.Model):
	# image = models.ImageField()
	# article = models.foreignkey

	def __unicode__(self):
		return smart_unicode(self.image)


class Like(models.Model):
	# image = models.ImageField()
	# article = models.foreignkey

	def __unicode__(self):
		return smart_unicode(self.image)


	
