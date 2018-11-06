from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

# Create your views here.


from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse("Hello, world. You're at the mbari deepseaweb index.")

def underground(request):
    return HttpResponse("This is the underground.")


