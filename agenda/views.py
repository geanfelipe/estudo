# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from agenda.forms import loginForm

def index(request):
	response = HttpResponse("Aqui esta o texto web")
	response.write("<h2> <a href='/usuariovalido'>Sou valido</a></h2>")
	if not request.user.is_authenticated():
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
	
	if request.method=='POST':
		username = request.POST['username']	
		password = request.POST['password']

		usuario = authenticate(username=username, password=password)

		if usuario:
			if usuario.is_active:
				login(request, usuario)
				response.write("<h3><a href='/'>logado bixo</a></h3>")
			else:
				response.write("<h3>Nao deu certo o login</h3>")
		else:
			response.write("<h1><a href='/'>Login inválido</a></h1>")
	else:
		return render(request, 'login.html',{})
