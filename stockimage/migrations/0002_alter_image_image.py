# Generated by Django 4.0.1 on 2022-01-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockimage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
