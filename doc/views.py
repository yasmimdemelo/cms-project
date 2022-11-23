from django.shortcuts import redirect, render
# from django.http import HttpResponse
from .models import Documents
from .form import DocumentsForm

def index(request):
    data = {}
    data['documents'] = Documents.objects.all()

    return render(request, 'doc/index.html', data)

def new_document(request):
    data = {}
    form = DocumentsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    data['form'] = form
    return render(request, 'doc/form.html', data)

def read(request, pk):
    data = {}
    data["documents"] = Documents.objects.filter(pk=pk)

    return render(request, 'doc/read.html', data)

def delete(request, pk):
    document = Documents.objects.get (pk=pk)
    if request.method == "POST":
        document.delete()
        return redirect('index')

    return render(request, 'index.html')