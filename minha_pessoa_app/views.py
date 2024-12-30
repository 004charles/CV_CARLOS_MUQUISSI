from django.shortcuts import render
from .models import Perfil, ExperienciaProfissional, AreaEspecializacao, Servico, Projeto
from django.core.exceptions import ValidationError
from PIL import Image
import os
from django.core.exceptions import ValidationError
from PIL import Image

def validate_image(value):
    try:
        img = Image.open(value)
        img.verify()
    except (IOError, SyntaxError):
        raise ValidationError('Envie uma imagem válida. O arquivo enviado não é uma imagem ou está corrompido.')

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png', '.gif']:
        raise ValidationError('Formato de imagem inválido. Aceitamos apenas JPG, JPEG, PNG e GIF.')


def home(request):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'home.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})


def sobre(request):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'sobre.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})

def servico(request):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    servicos = Servico.objects.all()
    return render(request, 'servico.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})


def work(request):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'work.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})

def detalhe_projecto(request, id):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'detalhe_projecto.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})

def blog(request):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'blog.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})

def detalhe_blog(request, id):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'detalhe_blog.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})