
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Comment(models.Model):
    """ Review model """
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='product_comments')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.product} review by {self.author}'

