from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category


# Register your models here.

class CategoryAdmin(TranslatableAdmin):
    list_display = ["category_name", "is_active", "is_delete", "created_at", "updated_at"]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
