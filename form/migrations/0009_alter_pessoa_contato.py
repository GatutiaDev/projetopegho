# Generated by Django 5.1.2 on 2024-10-27 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_alter_contato_cidade_alter_contato_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='contato',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pessoa', to='form.contato'),
        ),
    ]
