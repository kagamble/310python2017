"""
urls.py

The `urlpatterns` list routes URLs to views.

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

Including another URLconf
    1. from django.conf.urls import url, include
    2. Add the URL to urlpatterns:  url(r'^____/', include('____.urls'))
"""


from django.conf.urls     import url
from django.contrib       import admin                     #to do login/logout
from django.contrib.auth  import views as auth_views       #to do login/logout
from mandelbrot           import views

urlpatterns = [ url(r'^$',          views.HomePageView.as_view()),   #r'' is raw string
                url(r'^index',      views.HomePageView.as_view()),
                url(r'^code',       views.CodePageView.as_view()),
                url(r'^about',      views.AboutPageView.as_view()),

                url(r'^login',      views.LoginPageView.as_view()),
                url(r'^logout',     views.LogoutPageView.as_view()),

#               url(r'^profile',    views.ProfilePageView),

#                ^ means URL must match start of string
#                $ means URL must match end of string

#                url(r'^login/$',    auth_views.login,  name='login'),  
#                url(r'^logout/$',   auth_views.logout, name='logout'),
#                url(r'^admin/',     admin.site.urls),

#               url(r'^submit', views.PdfPageView.as_view()),
                url(r'^submit',     views.PdfPageView),

                url(r'^color',      views.ColorPageView),
                url(r'^newuser',    views.NewuserPageView),
              ]