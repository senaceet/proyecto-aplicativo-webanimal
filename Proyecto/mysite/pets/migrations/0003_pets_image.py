# Generated by Django 4.0 on 2022-03-06 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pets_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='image',
            field=models.ImageField(default='', upload_to='pets'),
            preserve_default=False,
        ),
    ]