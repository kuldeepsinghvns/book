from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse("hello")
