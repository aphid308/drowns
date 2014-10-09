from django.contrib import admin
from links.models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    fields = ('title', 'url')

admin.site.register(Link, LinkAdmin)