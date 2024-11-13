from django.shortcuts import render
from django.shortcuts import HttpResponse


def index_page(request):
    return render(request, 'base.html')