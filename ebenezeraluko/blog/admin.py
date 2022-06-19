from django.contrib import admin
from .models import Post

class PostDB(admin.ModelAdmin):
    list_display = [
        "post_title", "post_text", "created_date", "published_date"
    ]