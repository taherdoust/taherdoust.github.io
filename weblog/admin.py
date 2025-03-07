from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'classification', 'privacy', 'datetime')
    list_filter = ('classification', 'privacy')
    search_fields = ('title', 'passage')
