#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-12 17:18:24
# @Author  : ZFM (874051547@qq.com)
# @Link    : http://www.zhoufamig.web3v.com/
from django.conf import settings as original_settings
 
 
def settings(request):
    return {'settings': original_settings}
 
 
def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}