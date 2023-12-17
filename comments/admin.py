from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'product',
        'created_on',
        'rating',
    )

    ordering = ('-created_on',)


admin.site.register(Comment, CommentAdmin)
