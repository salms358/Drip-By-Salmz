# Generated by Django 3.2.22 on 2023-12-13 13:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users_likes',
            field=models.ManyToManyField(blank=True, related_name='favorite_products', to=settings.AUTH_USER_MODEL),
        ),
    ]