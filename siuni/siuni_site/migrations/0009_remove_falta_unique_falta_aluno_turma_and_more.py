# Generated by Django 4.2.16 on 2024-10-19 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siuni_site', '0008_remove_mediafinal_unique_media_aluno_turma_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='falta',
            name='unique_falta_aluno_turma',
        ),
        migrations.RemoveConstraint(
            model_name='mediafinal',
            name='unique_media_aluno_turma',
        ),
        migrations.RemoveField(
            model_name='falta',
            name='turma',
        ),
        migrations.AddField(
            model_name='falta',
            name='disciplina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='siuni_site.disciplina'),
        ),
        migrations.AddConstraint(
            model_name='falta',
            constraint=models.UniqueConstraint(fields=('aluno', 'disciplina'), name='unique_falta_aluno_disciplina'),
        ),
        migrations.AddConstraint(
            model_name='mediafinal',
            constraint=models.UniqueConstraint(fields=('aluno', 'disciplina'), name='unique_media_aluno_disciplina'),
        ),
    ]
