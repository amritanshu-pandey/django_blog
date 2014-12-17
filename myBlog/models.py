from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime
# Create your models here.

class Article(models.Model):
	USE_TZ = False
	title =models.CharField(max_length=140)
	date = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=140)
	content = models.TextField(blank=True)
	published = models.BooleanField(default=True)
	author = models.ForeignKey(User)
	link = models.URLField(blank=True)
	link_description=models.CharField(blank=True,max_length=140)
	slug = models.SlugField(max_length=140)
	def get_absolute_url(self):
		ret = '/blog/view/'+self.slug
		return (ret)
	def __unicode__(self):
		return (self.title)

class Categories(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	count = models.IntegerField(default=0)
	def __unicode__(self):
		return(self.name)
