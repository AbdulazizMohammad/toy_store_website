# Generated by Django 4.2.11 on 2024-04-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toymodule', '0009_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isLogged',
            field=models.BooleanField(default=False),
        ),
    ]
