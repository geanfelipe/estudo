# -*- condig: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate


def index(request):
	response = HttpResponse("Aqui esta o texto web")
	response.write("<h2> <a href='/login'>Login</h2>")
	return response

def login(request):
	usuario = authenticate(username='gean', password='123')
	response = HttpResponse()
	if usuario is not None:
		if usuario.is_active:
			response.write("Usuario valido")
		else:
			reponse.write("Usuario nao ativo")
	else:
		response.write("Algo incorreto")

	return response
			
