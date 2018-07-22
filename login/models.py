# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
      username=models.CharField(u'用户名',max_length=32,unique=True)
      password=models.CharField(max_length=64)
      realname=models.CharField(verbose_name='姓名',max_length=64,blank=True,null=True)
      choice_sex=(("M",u"Male"),("F",u"Female"),)
      gender = models.CharField(max_length=2, choices=choice_sex)
      qq=models.CharField(u'qq号',max_length=64,blank=True,null=True)
      phone=models.CharField(u'手机号',max_length=64,blank=True,null=True)
      email=models.EmailField(verbose_name="邮箱",blank=True,null=True)
      roles=models.ManyToManyField('Role',blank=True,null=True)
      createtime=models.DateField(u'创建时间',auto_now_add=True)#自增 对象创建时自动设置为当前时间，即创建日期
      updatetime=models.DateTimeField(u'更新时间',auto_now = True)#对象保存时自动设置为当前日期，即修改日期
      choice_statues=((True,'正常使用'),(False,'停止使用'),)
      statues=models.BooleanField(verbose_name='状态',default=True,choices=choice_statues)
      context=models.TextField(verbose_name="备注",blank=True,null=True)
      def __unicode__(self):
      	return self.username
      class Meta:
      	verbose_name_plural='用户表'
class Role(models.Model):
    Rname=models.CharField(verbose_name='角色',max_length=32,unique=True)
    menus=models.ManyToManyField("Menu",blank=True,null=True)
    def __unicode__(self):
      	return self.Rname
    class Meta:
      	verbose_name_plural='角色表'

class Menu(models.Model):
    Mname=models.CharField(max_length=32,verbose_name='菜单名')
    url_name=models.CharField(max_length=64,verbose_name='地址名')
    def __unicode__(self):
       return  self.Mname
    class Meta:
		verbose_name_plural='菜单表'