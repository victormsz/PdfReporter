from django.http import HttpResponse
from models import Template


def index(request):
    return HttpResponse("Reporter Index")

def templates(request):
    return HttpResponse("você está vendo templates existentes")

def templates_id(request,idtemplate):
    return HttpResponse("você está no %s template" % idtemplate)
