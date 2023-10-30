from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'display_categories',  # Replace 'category' with 'display_categories'
        'price',
        'rating',
        'image',
    )
    
    ordering = ('sku',)

    def display_categories(self, obj):
        """Display all categories associated with a product."""
        return ", ".join([category.name for category in obj.categories.all()])

    # This sets the column header for 'display_categories' method in the admin panel
    display_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
