from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Item, Shop, Purchase, PurchaseItem, ItemPrice


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'view_shops')

    def view_shops(self, obj):
        count = obj.shop_set.count()
        url = (
                reverse("admin:app_goods_shop_changelist")
                + "?"
                + urlencode({"item__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Shops</a>', url, count)

    view_shops.short_description = "Shops"


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'view_items_list')

    def view_items_list(self, obj):
        count = obj.items.count()
        url = (
                reverse("admin:app_goods_item_changelist")
                + "?"
                + urlencode({"shop__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Items</a>', url, count)

    view_items_list.short_description = "Items"


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    raw_id_fields = ['product']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date']
    inlines = [PurchaseItemInline]


class ItemPriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'shop', 'price', 'in_stock']


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(ItemPrice, ItemPriceAdmin)


