# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def index(request):
	response = HttpResponse("Aqui esta o texto web")
	response.write("<h2> <a href='/usuariovalido'>Sou valido</a></h2>")
	response.write("<h2><a href='login/'>login</a></h2>")
	return response

def usuarioValido(request):
	usuario = authenticate(username='gean', password='123')

	response = HttpResponse()
	if usuario is not None:
		if usuario.is_active:
			response.write("Usuario gean é valido")
		else:
			reponse.write("Usuario nao ativo")
	else:
		response.write("Algo incorreto")

	return response

def login(request):
	response = HttpResponse()
	if request.user.is_authenticated():
		response.write("você está autenticado")
	else:
		response.write("efetue o login")
