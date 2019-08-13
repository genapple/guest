#-*- coding:UTF-8 -*-
"""guest URL Configuration

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
from sign import views
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index), #添加index/路径配置
    url(r'^login_action/$',views.login_action), #添加index/路径配置
    url(r'^event_manage/$',views.event_manage), #添加index/路径配置
    url(r'^accounts/login/$',views.index), #添加index/路径配置
    url(r'^search_name/$',views.search_name), #添加search_name/路径配置
    url(r'^guest_manage/$',views.guest_manage), #添加index/路径配置
    url(r'^sign_index/(?P<eid>[0-9]+)/$', views.sign_index), #添加sign/路径配置
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action), #添加sign之后的跳转路径配置
    url(r'^logout/$', views.logout),#添加logout路径
    url(r'^api/',include('sign.urls', namespace='sign')),


]
