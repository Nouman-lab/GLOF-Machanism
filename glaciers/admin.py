from django.contrib import admin
from .models import Glacier

@admin.register(Glacier)
class GlacierAdmin(admin.ModelAdmin):
    list_display = ('name', 'volume', 'risk_level', 'created_at', 'updated_at')
    list_filter = ('risk_level', 'event_type')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at' 