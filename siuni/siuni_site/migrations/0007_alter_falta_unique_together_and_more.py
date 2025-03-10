# Generated by Django 4.2.16 on 2024-10-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siuni_site', '0006_alter_falta_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='falta',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='codigo_disciplina',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='codigo_turma',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddConstraint(
            model_name='avaliacao',
            constraint=models.UniqueConstraint(fields=('nome_avaliacao', 'data_avaliacao', 'hora_avaliacao', 'sala_avaliacao', 'predio_avaliacao', 'peso_avaliacao', 'turma'), name='unique_avaliacao_completa'),
        ),
        migrations.AddConstraint(
            model_name='falta',
            constraint=models.UniqueConstraint(fields=('aluno', 'turma'), name='unique_falta_aluno_turma'),
        ),
        migrations.AddConstraint(
            model_name='mediafinal',
            constraint=models.UniqueConstraint(fields=('aluno', 'turma'), name='unique_media_aluno_turma'),
        ),
        migrations.AddConstraint(
            model_name='nota',
            constraint=models.UniqueConstraint(fields=('avaliacao', 'aluno'), name='unique_nota_avaliacao_aluno'),
        ),
        migrations.AddConstraint(
            model_name='turma',
            constraint=models.UniqueConstraint(fields=('codigo_turma', 'hora_inicio', 'hora_fim', 'dias_semana', 'disciplina', 'professor'), name='unique_turma_completa'),
        ),
    ]
