# Generated by Django 3.1.5 on 2022-05-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_filme_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='duracao',
            field=models.IntegerField(null=True, verbose_name='Duração'),
        ),
    ]
