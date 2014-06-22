from django.contrib import admin

from myBlog.models import Article,Categories
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
#	fields=['name','description','parent_category']
	list_display=('name','description')
	list_filter=['name']

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article,ArticleAdmin)
admin.site.register(Categories,CategoriesAdmin)


