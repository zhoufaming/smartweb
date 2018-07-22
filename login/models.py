# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
      username=models.CharField(u'用户名',max_length=15)
      password=models.CharField(max_length=30)
      statues=models.IntegerField()
      createtime=models.DateField(u'创建时间',auto_now_add=True)
      updatetime=models.DateField(u'更新时间',auto_now = True)
      def __unicode__(self):
      	return self.username