from django.contrib import admin
from .models import (
    Categoria, Artigo, Comentario, RedeSocial, Projeto, Blog, Disponibilidade, 
    Contato, AreaEspecializacao, ExperienciaProfissional, Servico, SobreMim, Perfil, Marca, PremioReconhecimento
)

# Registrando todos os modelos com campos completos visíveis no admin

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'data_publicacao', 'atualizado_em')
    list_filter = ('categoria', 'autor')
    search_fields = ('titulo', 'descricao')
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'artigo', 'data_comentario', 'aprovado')
    list_filter = ('aprovado', 'artigo')
    search_fields = ('nome', 'texto')

@admin.register(RedeSocial)
class RedeSocialAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nome', 'url')
    search_fields = ('usuario__username', 'nome')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data_criacao')
    search_fields = ('titulo', 'descricao')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')

@admin.register(Disponibilidade)
class DisponibilidadeAdmin(admin.ModelAdmin):
    list_display = ('disponivel',)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('email', 'telefone', 'linkedin', 'github')
    search_fields = ('email', 'telefone')

@admin.register(AreaEspecializacao)
class AreaEspecializacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem')
    search_fields = ('nome', 'imagem')

@admin.register(ExperienciaProfissional)
class ExperienciaProfissionalAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'data_inicio', 'data_fim')
    search_fields = ('cargo', 'empresa')
    list_filter = ('empresa', 'data_inicio', 'imagem')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome',  'imagem')
    search_fields = ('nome', 'imagem')

@admin.register(SobreMim)
class SobreMimAdmin(admin.ModelAdmin):
    list_display = ('eu_sou', 'um', 'profissao', 'paixao', 'ou_profissao', 'com', 'ano_experiencia', 'ultima_des')
    search_fields = ('profissao', 'paixao')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'eu_sou','profissao','ou_profissao', 'com', 'ano_experiencia', 'ultima_des')
    search_fields = ('nome', 'profissao', 'imagem')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logotipo')
    search_fields = ('nome',)

@admin.register(PremioReconhecimento)
class PremioReconhecimentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data_recebimento')
    search_fields = ('titulo', 'descricao')


from .models import Contactar

class ContactarAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'mensagem')  # Campos a serem exibidos na lista
    search_fields = ('nome', 'email', 'assunto')  # Campos pesquisáveis
    list_filter = ('assunto',)  # Filtros para o Admin

admin.site.register(Contactar, ContactarAdmin)
