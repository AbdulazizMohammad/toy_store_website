# Generated by Django 4.2.11 on 2024-05-17 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toymodule', '0012_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(upload_to=''),
        ),
    ]
