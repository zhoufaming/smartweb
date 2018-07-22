# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datadeal import Exceltool
import pythoncom
ip=[]
# Create your views here.
def logstatics(request):
    pythoncom.CoInitialize()
    obj=Exceltool()
    Context=obj.exceldata()
    return render(request,"tables.html",{'Context':Context} ) #,'ip':ip,'data':Context['data']})