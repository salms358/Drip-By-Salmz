# Generated by Django 3.2.22 on 2024-01-23 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_users_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shoe_size',
        ),
        migrations.AddField(
            model_name='product',
            name='is_shoe',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ShoeSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoe_sizes', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sizes', to='products.product')),
            ],
        ),
    ]
