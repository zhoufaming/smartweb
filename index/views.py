# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# def auth(func):
#     def inner(reqeust,*args,**kwargs):
#         v = reqeust.COOKIES.get('user')
#         if not v:
#             return HttpResponseRedirect('/login/')
#         return func(reqeust, *args,**kwargs)
#     return inner
# @login_required(login_url='/login/')
# @auth
def index_fuc(request):
	return render (request,'index.html')
# Create your views here.


