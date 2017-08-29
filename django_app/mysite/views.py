from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Bilateral


def index(request):
    return render(request, 'mysite/index.html')

def data(request):
    bilateral_list = Bilateral.objects.all()[:100]
    context = {
        'bilateral_list': bilateral_list,
    }
    return render(request, 'mysite/data.html', context)

def detail(request, record_id):
    context = {
        'record_id': record_id,
    }
    return render(request, 'mysite/detail.html', context)

def pdf_view(request):
    return FileResponse(open('mysite/templates/mysite/resume.pdf', 'rb'), content_type='application/pdf')
