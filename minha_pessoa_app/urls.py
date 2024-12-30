from django.urls import path
from minha_pessoa_app import views

urlpatterns = [
    path('sobre/', views.sobre, name = 'sobre'),
    path('servico/', views.servico, name = 'servico'),
    path('work/', views.work, name = 'work'),
    path('detalhe_projecto/<int:id>', views.detalhe_projecto, name = 'detalhe_projecto'),
    path('blog/', views.blog, name = 'blog'),
    path('detalhe_blog/<int:id>', views.detalhe_blog, name = 'detalhe_blog'),
    path('contactar/', views.contactar, name = 'contactar'),
    path('salvar_comentario/<int:artigo_id>/', views.salvar_comentario, name='salvar_comentario'),
    
]
