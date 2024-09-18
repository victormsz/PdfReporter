# Generated by Django 5.1 on 2024-08-26 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('idadministrador', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('senha', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('idempresa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('idsitio', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('CEP', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('idtecnico', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('idfoto', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('descricao', models.TextField()),
                ('metadados', models.JSONField()),
                ('idsitio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.sitio')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('idtemplate', models.AutoField(primary_key=True, serialize=False)),
                ('pedidos_fotos', models.JSONField()),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.administrador')),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='relatorio_final',
            fields=[
                ('idrelatorio_final', models.AutoField(primary_key=True, serialize=False)),
                ('endereco_server', models.CharField(max_length=150)),
                ('data', models.DateField()),
                ('data_visita', models.DateField()),
                ('Foto', models.ManyToManyField(to='reporter.foto')),
                ('idsitio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.sitio')),
                ('tecnico_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.tecnico')),
                ('idtemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.template')),
            ],
        ),
    ]
