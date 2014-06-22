from django.conf.urls import patterns,url
from myBlog import views
from django.contrib import admin

urlpatterns = [
	url(r'^$',views.index,name='blog'),
	url(r'^category',views.viewCategories,name='category'),
	url(r'^view/(?P<slug>[^\.]+)',views.view_posts,name='view_blog_post')
]
