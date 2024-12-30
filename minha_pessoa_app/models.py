from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Modelo para Categorias de Artigos
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

# Modelo para Artigos
class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    descricao = models.TextField()
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='artigos')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='artigos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

# Modelo para Comentários
class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'Comentário de {self.nome} em {self.artigo}'

# Modelo para Redes Sociais
class RedeSocial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='redes')
    nome = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.nome} de {self.usuario}'

# Modelo para Projetos
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    link = models.URLField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    views_imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)


    def __str__(self):
        return self.titulo


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Disponibilidade(models.Model):
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return "Disponível" if self.disponivel else "Não Disponível"

class Contato(models.Model):
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email

class AreaEspecializacao(models.Model):
    imagem = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ExperienciaProfissional(models.Model):
    imagem = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"

class Servico(models.Model):
    imagem = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class SobreMim(models.Model):
    eu_sou = models.CharField(max_length=100)
    um = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    paixao = models.CharField(max_length=100)
    ou_profissao = models.CharField(max_length=100)
    com = models.CharField(max_length=100)
    ano_experiencia = models.CharField(max_length=100)
    ultima_des = models.TextField()

class Perfil(models.Model):
    imagem = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    nome = models.CharField(max_length=100)
    eu_sou = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    ou_profissao = models.CharField(max_length=100)
    com = models.CharField(max_length=100)
    ano_experiencia = models.CharField(max_length=100)
    ultima_des = models.TextField()
    

    def __str__(self):
        return "Sobre Mim"

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='marcas/', blank=True, null=True)

    def __str__(self):
        return self.nome

class PremioReconhecimento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_recebimento = models.DateField()

    def __str__(self):
        return self.titulo