# Generated by Django 5.1.2 on 2024-10-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_alter_contato_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(help_text='exemplo@email.com', max_length=254, unique=True),
        ),
    ]
