from django.conf.urls import include,patterns,url
from myBlog import views
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
        url(r'^blog/',include('myBlog.urls')),
	url(r'^admin/', include(admin.site.urls),name='admin'),
]

