# Generated by Django 3.0.3 on 2020-05-31 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_testers', '0002_auto_20200530_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roteiro',
            name='cenarios',
            field=models.ManyToManyField(to='for_testers.Cenario'),
        ),
        migrations.AlterField(
            model_name='roteiro',
            name='projetos',
            field=models.ManyToManyField(to='for_testers.Projeto'),
        ),
    ]
