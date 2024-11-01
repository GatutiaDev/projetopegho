# Generated by Django 5.1.2 on 2024-10-26 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_contato_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(help_text='exemplo@email.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='O número de telefone deve conter apenas dígitos.', regex='^\\d{10,15}$')]),
        ),
    ]
