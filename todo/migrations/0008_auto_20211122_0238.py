# Generated by Django 3.1.5 on 2021-11-22 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20211122_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalizado', models.BooleanField()),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.usuario', verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.filme', verbose_name='Filme')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.pedido', verbose_name='Pedido')),
            ],
        ),
    ]
