# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import agenda.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', agenda.views.index, name = "index"),
    url(r'^usuariovalido/', agenda.views.usuarioValido, name = 'usuarioValido')
#    url(r'^login/', agenda.views.login, name= 'login'),


)
