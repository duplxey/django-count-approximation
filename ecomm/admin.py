from django.contrib import admin

from ecomm.models import Product, Purchase
from ecomm.paginators import PreviousNextPaginator


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]
    search_fields = ["name", "description"]


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["__str__", "first_name", "last_name", "created_at", "updated_at"]
    search_fields = ["product__name", "first_name", "last_name", "address"]
    list_filter = ["product"]
    paginator = PreviousNextPaginator

    def get_queryset(self, request):
        return super().get_queryset(request)


admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
