# -*- coding: utf-8 -*-
from django.http  import HttpResponse

from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>music website</h1>")
