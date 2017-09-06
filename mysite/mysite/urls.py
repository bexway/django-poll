"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # include gives the option for adding more detail to the url, and should be used in almost every case. admin.site.urls is an exception.
    # the url function takes 4 arguments:
    # 1) a regex for finding that url (will look for polls/, so further stuff can follow)
    # 2) a view function, with an HttpRequest object as the first argument and any values from the regular expression as other arguments
    # 3 and 4) optional keyword and name arguments, for adding keywords and giving the url a global name
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
