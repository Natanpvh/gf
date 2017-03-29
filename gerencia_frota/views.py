from django.shortcuts import render
from django.utils import timezone
from .models import TipoVeiculo

# Create your views here.
def index(request):
    tipoveiculos = TipoVeiculo.objects.all()
    return render(request, 'index.html', {'tipoveiculos' : tipoveiculos})
