from django.shortcuts import render,get_object_or_404
from myBlog.models import Categories,Article
from django.http import HttpResponse
# Create your views here.
def viewCategories(request):
	v_categories=Categories.objects.all()
	context={'v_categories':v_categories}
	return render(request,'view_categories.html',context)
	
def index(request):
	v_articles=Article.objects.order_by("date").reverse()
	context={'v_articles':v_articles}
	return render(request,'view_articles.html',context)

def view_posts(request,slug):
	v_articles=Article.objects.filter(slug=slug)
	context={'v_articles':v_articles}
	return render(request,'view_aticles_details.html',context)
