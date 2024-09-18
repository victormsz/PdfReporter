from django.test import TestCase
from django.http import HttpResponse

def index(request):
    return HttpResponse("Report Index")

# Create your tests here.
