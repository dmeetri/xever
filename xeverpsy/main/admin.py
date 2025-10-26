from django.contrib import admin
from .models import *

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video', 'upload_at')
    search_fields = ("title", "description")
    list_filter = ("title", 'upload_at')
    list_per_page = 50
    ordering = ("-id",)