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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import re_path
from django.contrib import admin
from mysite import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^histogram/', views.freQ),
    re_path(r'^display/', views.search_form),
    re_path(r'^search/', views.search),
    re_path(r'^hello/$', views.hello),
    re_path(r'^time/$', views.current_datetime),
    re_path(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    re_path(r'^latest/$', views.latest_books),
    re_path(r'^meta/$', views.display_meta),
    re_path(r'^search-form/$', views.search_form),
    re_path(r'^search/$', views.search),
    re_path(r'^contact-form/$', views.contact_form),
    re_path(r'^contact/$', views.contact),
    re_path(r'^contactV2/$', views.contact_formsframework),
    re_path(r'^contact/thanks/$', views.hello),
    re_path(r'^addauthor/$', views.addauthor),
    re_path(r'^all-authors/$', views.all_authors),

    # Assignment [3] part
    #=================================================
    re_path(r'^$', views.home),
    re_path(r'^teacher/$', views.addteacher),
    re_path(r'^student/$', views.addstudent),
    re_path(r'^course/$', views.addcourse), re_path(r'^teachersuccess/$', views.succesteacher),
    re_path(r'^coursesuccess/$', views.succescourse), re_path(r'^studentssuccess/$', views.successtudent)
    #=================================================

]
