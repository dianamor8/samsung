from http.client import HTTPResponse
from multiprocessing import context
from re import template
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from recurso.models import Resource
# Create your views here.


def index(request):
    return HttpResponse("Hola esta es mi página de recursos")


def detail(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    if resource is not None:
        return render(request, 'resources/resource.html', {'resource', resource})
    else:
        raise Http404('Resource does not exist')


def index(request):
    resources_list = Resource.objects.all()    
    if (resources_list):
        context = {
            'resource_list': resources_list,
        }
        return render(request, 'recurso/index.html', context)
    else:
        raise Http404('No hay recursos disponibles')