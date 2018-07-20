# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
class ContactForm(forms.Form):
    subject=models.CharField(max_length=30)