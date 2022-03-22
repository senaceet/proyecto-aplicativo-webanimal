# Generated by Django 3.2.6 on 2022-03-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('number', models.IntegerField(max_length=20, verbose_name='Numero')),
                ('issue', models.TextField(max_length=500, verbose_name='Asunto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]