from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    categories = models.ManyToManyField('Category', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    is_shoe = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    users_likes = models.ManyToManyField(User,
                                         related_name='favorite_products',
                                         blank=True)
    shoe_size = models.IntegerField(
        null = True,
        blank = True,
    )

    product_size = models.CharField(
        max_length = 2,
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.name

class Meta:
    constraints = [
        models.CheckConstraint(
            check=models.Q(has_sizes=True, is_shoe=False) | models.Q(has_sizes=False, is_shoe=True),
            name='one_of_has_sizes_or_is_shoe'
        ),
        models.UniqueConstraint(
            fields=['has_sizes', 'is_shoe'],
            condition=models.Q(has_sizes=True, is_shoe=True),
            name='unique_has_sizes_and_is_shoe'
        ),
    ]

    def save(self, *args, **kwargs):
        if self.has_sizes and self.is_shoe or not self.has_sizes and not self.is_shoe:
            raise IntegrityError('Only one of the 2 sizes can be True')

        
        super().save(*args, **kwargs)