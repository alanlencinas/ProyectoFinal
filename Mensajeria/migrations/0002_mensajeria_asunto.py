# Generated by Django 4.2.3 on 2023-09-21 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajeria',
            name='asunto',
            field=models.TextField(default='Sin Asunto'),
        ),
    ]
