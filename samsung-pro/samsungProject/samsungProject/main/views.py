from recurso.models import Resource
from django.shortcuts import render

def homepage(request):    
    resources_list = Resource.objects.all()
    # resources_list = Resource.objects.get(status=True)    
    if (resources_list):
        context = {
            'resource_list': resources_list,
        }
        return render(request, 'index.html', context)    