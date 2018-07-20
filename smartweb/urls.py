"""smartweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from login import views as loginView
from index import views as indexView
from django.conf import settings
from django.conf.urls import include

# from django.views.generic.simple import redirect_to 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',loginView.user_login,name='login'),
    url(r'^index/',indexView.index_fuc,name='index'),
    url(r'',loginView.user_login,name="login"),


    
]
if settings.DEBUG: 
	import debug_toolbar 
	urlpatterns = [
url(r'^debug/', include(debug_toolbar.urls)), ] + urlpatterns 