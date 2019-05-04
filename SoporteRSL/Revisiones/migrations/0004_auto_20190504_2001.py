# Generated by Django 2.2 on 2019-05-04 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revisiones', '0003_auto_20190501_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='titulo',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revision',
            name='investigadores',
            field=models.ManyToManyField(to='Investigadores.Investigador', verbose_name='Investigadores'),
        ),
    ]
