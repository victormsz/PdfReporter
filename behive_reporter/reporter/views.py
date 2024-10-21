from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy  
from django.views.generic import CreateView 
from .models import TemplateRelatorio, Foto  # Imports corrigidos e 
import os
from django.conf import settings

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "reporter/signup.html"

def index(request):
    return HttpResponse("Reporter Index")

def templates(request):
    return HttpResponse("Você está vendo templates existentes")

def templates_id(request, idtemplate_relatorio):
    return HttpResponse(f"Você está no template {idtemplate_relatorio}")

def generate_pdf(request, idfoto):
    # Obter o objeto da foto pelo seu id ou retornar 404 se não encontrado
    foto = get_object_or_404(Foto, idfoto=idfoto)

    # Criar o caminho absoluto da imagem
    caminho_absoluto = os.path.join(settings.MEDIA_ROOT, foto.foto.name)  # Use 'foto.foto.name' para obter o caminho correto

    # Iniciar a criação do PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Adicionar conteúdo ao PDF
    pdf.drawString(100, 750, f"Descrição: {foto.descricao}")
    pdf.drawString(100, 730, f"Caminho da Foto: {foto.caminho}")

    # Adicionando a imagem ao PDF, verificando se o caminho é válido
    try:
        pdf.drawImage(caminho_absoluto, 100, 500, width=200, height=200)
    except Exception as e:
        pdf.drawString(100, 500, "Erro ao carregar a imagem: " + str(e))

    # Finalizar o PDF
    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    # Retornar o PDF como resposta
    return HttpResponse(buffer, content_type='application/pdf')