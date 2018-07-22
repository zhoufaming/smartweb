# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User
from .models import Role
from .models import Menu
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display =('username','realname','gender','phone','qq','updatetime','createtime','statues')
    list_editable=('statues',)
    list_filter=('statues',)
admin.site.site_header = 'SmartWeb后台管理系统'  # 此处设置页面显示标题
admin.site.site_title = 'SmartWeb'  # 此处设置页面头部标题
admin.site.register(User,UserAdmin)
admin.site.register(Role) 
admin.site.register(Menu) 