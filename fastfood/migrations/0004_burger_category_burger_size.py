# Generated by Django 5.0.1 on 2024-06-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfood', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='burger',
            name='category',
            field=models.CharField(default='Fajita', max_length=120),
        ),
        migrations.AddField(
            model_name='burger',
            name='size',
            field=models.CharField(default='M', max_length=120),
        ),
    ]