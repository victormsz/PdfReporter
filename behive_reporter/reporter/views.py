from django.http import HttpResponse
from io import BytesIO
from .models import TemplateRelatorio  # Corrected import
from .models import Foto  # Corrected import
from django.db import models
from reportlab.pdfgen import canvas
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy  
from django.views.generic import CreateView 


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "reporter/signup.html"

def index(request):
    return HttpResponse("Reporter Index")


def templates(request):
    return HttpResponse("Você está vendo templates existentes")


def templates_id(request, idtemplate_relatorio):  # Corrected parameter name
    return HttpResponse(f"Você está no template {idtemplate_relatorio}")  # Using f-string for better formatting

def generate_pdf(request, idfoto):
    # Get the photo object by its id
    Foto = Foto.objects.get(id=idfoto)
    
    # Start creating the PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    
    # Add some content, for example, the photo address and the image itself
    pdf.drawString(100, 800, f"Desccricao: {Foto.descricao}")
    pdf.drawString(100, 780, f"Photo Path: {Foto.caminho}")
    
    # Assuming the image is stored in the 'media' folder, you can add it to the PDF
    pdf.drawImage(Foto.caminho, 100, 600, width=200, height=200)
    
    # Finalize the PDF
    pdf.showPage()
    pdf.save()
    
    buffer.seek(0)
    
    # Return the PDF as a response
    return HttpResponse(buffer, content_type='application/pdf')

