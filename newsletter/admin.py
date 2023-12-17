
from django.contrib import admin
from .models import Subscriber

class NewsletterAdmin(admin.ModelAdmin):
    newsletter = ('email', 'time_subscribed')  

admin.site.register(Subscriber, NewsletterAdmin)