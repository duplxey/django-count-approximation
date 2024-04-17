from django.contrib import admin

from ecomm.models import Product, Purchase


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]
    search_fields = ["name", "description"]


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["__str__", "product", "first_name", "last_name", "created_at", "updated_at"]
    list_select_related = ["product"]
    list_filter = ["product"]
    search_fields = ["product__name", "first_name", "last_name", "address"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
