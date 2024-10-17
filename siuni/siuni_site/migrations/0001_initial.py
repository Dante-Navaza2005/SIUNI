# Generated by Django 4.2.16 on 2024-10-16 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_documento', models.CharField(blank=True, max_length=200, null=True)),
                ('data_nascimento', models.CharField(blank=True, max_length=200, null=True)),
                ('cpf', models.CharField(blank=True, max_length=200, null=True)),
                ('rg', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('telefone', models.CharField(blank=True, max_length=200, null=True)),
                ('tipo_de_usuario', models.CharField(choices=[('Aluno', 'Aluno'), ('Professor', 'Professor')], max_length=50)),
                ('documento', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='siuni_site.documento')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('matricula', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('coordenador', models.BooleanField(default=False)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professor', to='siuni_site.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='aluno', to='siuni_site.usuario')),
            ],
        ),
    ]