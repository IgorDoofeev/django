from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Это страница приложения Women.')


def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')
