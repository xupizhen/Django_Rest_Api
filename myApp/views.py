from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import JsonResponse


def index(request):
    # raise Exception("这是一个错误")
    return HttpResponse("sunck is a good man")
