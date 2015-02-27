# -*- condig: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse


def index(request):
	response = HttpResponse("Aqui esta o texto web")
	response.write("<h2> <a href='/login'>Login</h2>")
	return response
