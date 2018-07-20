# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.template.context_processors import csrf
from models import User
from django import forms
from django.views.decorators.cache import cache_page
from django.utils.translation import ugettext
from django.shortcuts import redirect 
class UserForm(forms.Form):# 表单类 可单独生成一个文件 forms.py
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
@cache_page(60 * 5) # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def user_login(request):
    if request.method == 'POST':
    	useinfo=UserForm(request.POST)# form 包含提交的数据
    	if useinfo.is_valid():# 如果提交的数据合法
           username = useinfo.cleaned_data['username']
           password = useinfo.cleaned_data['password']
           # user = User.model.objects.get(username=username, password=password)
           user = User.objects.filter(username = username,password= password)

        if user :
            # return render_to_response('index.html',context=csrf(request))
            return HttpResponseRedirect('/index/')
            res= HttpResponseRedirect('/index/')
            # res= HttpResponse('/index/')
            res.set_cookies('user',username,max_age=3600)
            return res
           
        else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
        return render_to_response('login.html',context=csrf(request))
    # return render(request,"index.html",  {})
# Create your views here.
