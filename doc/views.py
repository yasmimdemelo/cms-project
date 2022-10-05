from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {}
    data['documents'] = ['Doc01', 'Doc02', 'Doc03', 'Doc04']

    return render(request, 'doc/index.html', data)