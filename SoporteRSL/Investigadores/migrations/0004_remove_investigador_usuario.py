# Generated by Django 2.2 on 2019-05-01 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Investigadores', '0003_investigador_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigador',
            name='usuario',
        ),
    ]
