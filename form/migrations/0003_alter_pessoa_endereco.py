# Generated by Django 5.1.2 on 2024-10-24 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_experiencia_pessoa_formacao_pessoa_pessoa_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pessoas', to='form.contato'),
        ),
    ]