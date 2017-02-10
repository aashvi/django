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