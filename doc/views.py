from django.shortcuts import render
from django.http import HttpResponse
from .models import Documents

def index(request):
    data = {}
    data['documents'] = Documents.objects.all()

    return render(request, 'doc/index.html', data)