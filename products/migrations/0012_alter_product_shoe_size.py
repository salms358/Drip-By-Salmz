# Generated by Django 3.2.22 on 2024-02-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_shoe_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shoe_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]