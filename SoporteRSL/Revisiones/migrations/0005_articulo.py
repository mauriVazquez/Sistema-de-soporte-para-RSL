# Generated by Django 2.2 on 2019-06-03 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Revisiones', '0004_auto_20190504_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('leido', models.BooleanField(default=False, verbose_name='¿El articulo fue leeido?')),
                ('archivo', models.FileField(upload_to='articulos/')),
                ('revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revisiones.Revision')),
            ],
        ),
    ]