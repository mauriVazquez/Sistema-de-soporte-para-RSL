# Generated by Django 2.2 on 2019-06-25 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Investigadores', '0005_investigador_usuario'),
        ('Revisiones', '0008_revision_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('investigador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Investigadores.Investigador')),
                ('revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revisiones.Revision')),
            ],
            options={
                'verbose_name_plural': 'Modificaciones',
            },
        ),
    ]
