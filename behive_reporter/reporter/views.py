from django.http import HttpResponse
from .models import TemplateRelatorio  # Corrected import


def index(request):
    return HttpResponse("Reporter Index")


def templates(request):
    return HttpResponse("Você está vendo templates existentes")


def templates_id(request, idtemplate_relatorio):  # Corrected parameter name
    return HttpResponse(f"Você está no template {idtemplate_relatorio}")  # Using f-string for better formatting
