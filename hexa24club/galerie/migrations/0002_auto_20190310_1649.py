# Generated by Django 2.1.5 on 2019-03-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
