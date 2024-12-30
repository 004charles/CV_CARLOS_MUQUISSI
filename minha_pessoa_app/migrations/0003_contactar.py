# Generated by Django 5.1.4 on 2024-12-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_pessoa_app', '0002_alter_comentario_artigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('assunto', models.CharField(max_length=200)),
                ('mensagem', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
