# Generated by Django 4.2.16 on 2024-11-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siuni_site', '0011_alter_usuario_matricula_alter_usuario_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('autor', models.CharField(blank=True, max_length=200, null=True)),
                ('legenda', models.CharField(blank=True, max_length=200, null=True)),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
