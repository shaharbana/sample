"""example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from site_admin import views as adminview

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',adminview.index,name='index'),
    url(r'^Register/$',adminview.Register,name='Register'),
    url(r'^registerAction/$',adminview.registerAction,name='registerAction'),
    url(r'^Login/$',adminview.Login,name='Login'),
    url(r'^loginAction/$',adminview.loginAction,name='loginAction'),
    url(r'^viewAllUsers/$',adminview.viewAllUsers,name='viewAllUsers'),
    url(r'^approve/(?P<uid>\d+)/$',adminview.approve,name='approve'),
    url(r'^reject/(?P<uid>\d+)/$',adminview.reject,name='reject'),
    url(r'^EditProfile/$',adminview.EditProfile,name='EditProfile'),
    url(r'^EditProfileAction/$',adminview.EditProfileAction,name='EditProfileAction'),
    url(r'^delete/(?P<uid>\d+)/$',adminview.delete,name='delete'),
    url(r'^AddReview/$',adminview.AddReview,name='AddReview'),
    url(r'^addReviewAction/$',adminview.addReviewAction,name='addReviewAction'),
    url(r'^ViewReview/$',adminview.ViewReview,name='ViewReview'),
    url(r'^html2pdf/$',adminview.html2pdf,name='html2pdf'),
]
