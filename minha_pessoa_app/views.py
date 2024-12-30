from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfil, ExperienciaProfissional, AreaEspecializacao, Servico, Projeto,Blog, Comentario,  Disponibilidade, Projeto
from django.core.exceptions import ValidationError
from PIL import Image
from django.conf import settings
from django.http import HttpResponse
from .models import Contactar
from django.contrib.auth.models import User
from django.core.mail import send_mail
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
    blog = Blog.objects.all()
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'sobre.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos, 'blog':blog})

def servico(request):
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    disponibilidade = Disponibilidade.objects.first()
    servicos = Servico.objects.all()
    return render(request, 'servico.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos, 'disponibilidade': disponibilidade})


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
    projectos = get_object_or_404(Projeto, id=id)
    return render(request, 'detalhe_projecto.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos})

def blog(request):
    blog = Blog.objects.all()
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'blog.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos, 'blog':blog})

def detalhe_blog(request, id):
    comentario = Comentario.objects.all()
    blog = get_object_or_404(Blog, id=id)
    perfil = Perfil.objects.all()
    area = AreaEspecializacao.objects.all()
    servicos = Servico.objects.all()
    exprofissional = ExperienciaProfissional.objects.all()
    projectos = Projeto.objects.all()
    return render(request, 'detalhe_blog.html', {'perfil':perfil, 'exprofissional':exprofissional, 'area':area, 'servicos':servicos, 'projectos':projectos, 'blog':blog, 'comentario':comentario})


def salvar_comentario(request, artigo_id):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        texto = request.POST.get('texto')
        
        artigo = Blog.objects.get(id=artigo_id)
        
        comentario = Comentario(artigo=artigo, nome=nome, email=email, texto=texto)
        comentario.save()

        return redirect('detalhe_blog', id=artigo_id)  # redireciona para a página do blog, ou a página que você quiser

    return HttpResponse("Método não permitido.", status=405)


def contactar(request):
    perfil = Perfil.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        # Verificação simples para garantir que os campos não estão vazios
        if nome and email and assunto and mensagem:
            # Criando o objeto e salvando no banco de dados
            contactar_obj = Contactar(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
            contactar_obj.save()

            # Pegando o e-mail do superusuário (admin)
            try:
                admin_user = User.objects.filter(is_superuser=True).first()  # Pega o primeiro superusuário
                if admin_user:
                    admin_email = admin_user.email  # E-mail do superusuário
                else:
                    admin_email = settings.EMAIL_HOST_USER  # Se não encontrar um superusuário, usa o e-mail configurado
            except User.DoesNotExist:
                admin_email = settings.EMAIL_HOST_USER  # Caso não encontre, usa o e-mail de configuração

            # Enviando o e-mail
            subject = f"Nova mensagem de contato: {assunto}"
            message = f"Você recebeu uma nova mensagem de {nome} ({email}).\n\nMensagem:\n{mensagem}"
            from_email = settings.EMAIL_HOST_USER  # O e-mail que irá enviar
            recipient_list = [admin_email]  # O e-mail do admin ou do superusuário

            send_mail(subject, message, from_email, recipient_list)

            # Redireciona ou exibe uma mensagem de sucesso
            return HttpResponse('Mensagem enviada com sucesso!', content_type='text/plain')
        else:
            return HttpResponse('Todos os campos são obrigatórios. Tente novamente.', content_type='text/plain')

    return render(request, 'contacto.html',{'perfil':perfil})