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
from django.conf.urls import url
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^histogram/', views.freQ),
    url(r'^display/', views.search_form),
    url(r'^search/', views.search),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^latest/$', views.latest_books),
    url(r'^meta/$',views.display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact-form/$', views.contact_form),
    url(r'^contact/$', views.contact),
    url(r'^contactV2/$', views.contact_formsframework),
    url(r'^contact/thanks/$', views.hello),
    url(r'^addauthor/$',views.addauthor),
    url(r'^all-authors/$',views.all_authors),

    # Assignment [3] part
    #=================================================
    url(r'^$', views.home),
    url(r'^teacher/$', views.addteacher),
    url(r'^student/$', views.addstudent),
    url(r'^course/$', views.addcourse),url(r'^teachersuccess/$', views.succesteacher),url(r'^coursesuccess/$', views.succescourse),url(r'^studentssuccess/$', views.successtudent)
    #=================================================

]
