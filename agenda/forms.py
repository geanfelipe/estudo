# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class loginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password')
