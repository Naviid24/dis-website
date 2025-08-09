from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "email", "phone", "created_at")
    readonly_fields = ("created_at",)
