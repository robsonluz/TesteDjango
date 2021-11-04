# Generated by Django 3.1.5 on 2021-11-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
    ]