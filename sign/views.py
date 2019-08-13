# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sign.models import  Event,Guest

from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import  auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
import  os,django


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guest.settings")
# django.setup()
# Create your views here.
def index(request):
    # return HttpResponse("Hello Django")
    return render(request,"index.html")
def login_action(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        print username
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)#直接引用用户认证和登陆的相关方法

        # if username=='admin' and password=='admin123':
        #     # return HttpResponse('login sucess!')
        #     response=HttpResponseRedirect("/event_manage/")
        #     # response.set_cookie('user',username,3600)#添加浏览器cookie
        #     # return HttpResponseRedirect('/event_manage/')
        #     request.session['user']=username#将session 信息记录到浏览器
        #     return response
        if user is not None:
            auth.login(request,user)#调用自带的login 函数
            request.session['user']=username#将session 记录到浏览器
            response=HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})
@login_required
def event_manage(request):
    # username=request.COOKIES.get('user','')#读取浏览器cookie 信息

    event_list=Event.objects.all()
    username = request.session.get('user', '')
    return render(request,'event_manage.html',{"user":username,"events":event_list})
@login_required
def search_name(request):
    username=request.session.get('user', '')
    search_name=request.GET.get("name", "")
    event_list=Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})
# @login_required
# def guest_manage(request):
#     username=request.session.get('user','')
#     guest_list=Guest.objects.all()
#     return render(request,"guest_manage.html",{"user":username,"guests":guest_list})
@login_required
def guest_manage(request):
    username=request.session.get('user','')
    guest_list=Guest.objects.all()
    paginator=Paginator(guest_list,2)
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        #如果 page不是整数，取第一页面数据
        contacts=paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user":username,"guests":contacts})
#签到页面
@login_required
def sign_index(request,eid):
    event=get_object_or_404(Event,id=eid)
    return render(request,'sign_index.html',{'event':event})
@login_required
def sign_index_action(request,eid):
    event=get_object_or_404(Event, id=eid)
    phone=request.POST.get('phone','')
    print (phone)
    result=Guest.objects.filter(phone=phone)#使用过滤器查找是否有对应的结果
    if not result:
        return render(request,'sign_index.html',{'event': event, 'hint': ' phone error.'})
    result=Guest.objects.get(phone=phone, event_id=eid)#在指定的事件中找到指定的记录
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'event id og phone error. '})
    result=Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request,'sign_index.html',{'event': event, "hint":"user has sign in."})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign="1")
        return render(request,'sign_index.html',{"event":event,
                                                "hint":"sign in sucess",
                                                "guest": result })
@login_required
def logout(request):
    auth.logout(request)#退出登录
    response=HttpResponseRedirect('/index/')
    return response








