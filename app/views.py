from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Index hello')
    return render(request, 'app/index.html', {
        'title': 'Latest'
    })


"""DEMO HOMEPAGES FOR REVIEW"""

from django.views import generic

class TESTER_homea(generic.TemplateView):
    template_name = "app/demoHomepages/home_a.html"



