# Generated by Django 4.2.11 on 2024-03-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toymodule', '0006_alter_product_prduct_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prduct_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
