# Generated by Django 3.2.22 on 2024-02-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]