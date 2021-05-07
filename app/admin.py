from django.contrib import admin
from app.models import *
from app.admin_mixin import MultiDBModelAdmin


class OrdersAmdin(admin.ModelAdmin):
    model = Orders

    list_display = ["id", "name", "t_number", "date_created", "status", "date_ready", "note", "geography"]
    list_editable = ("status", "note", "geography")


class ProductsAmdin(admin.ModelAdmin):
    model = Products

    list_display = ["id", "title", "description", "image", "is_active"]


class CommentsAmdin(admin.ModelAdmin):
    model = Comments

    list_display = ["id", "name", "description", "photo", "date_created", "is_active", "rating"]


class SubscribeAmdin(admin.ModelAdmin):
    model = Subscribe

    list_display = ["id", "email", "date_created"]


class StockInline(admin.StackedInline):
    model = Stock
    extra = 0

    def has_add_permission(self, request, _):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PortInline(admin.StackedInline):
    model = Port
    extra = 0

    def has_add_permission(self, request, _):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class RegionAdmin(MultiDBModelAdmin):

    model = Region

    exclude = ("descripton",)
    readonly_fields = ("name",)
    list_display = ("name",)
    inlines = [StockInline, PortInline]


class WholeSaleAdmin(MultiDBModelAdmin):
    model = WholeSale
    list_display = ("id", "title", "subtitle", "price", "is_active")


class RetailSalesAdmin(MultiDBModelAdmin):
    model = RetailSales
    list_display = ("id", "title", "subtitle", "price", "is_active")



admin.site.register(Region, RegionAdmin)

title = "M3 Opt"
admin.site.site_title = title
admin.site.site_header = title
admin.site.index_title = "Админ панель M3 Opt"


admin.site.register(WholeSale, WholeSaleAdmin)
admin.site.register(RetailSales, RetailSalesAdmin)
admin.site.register(Orders, OrdersAmdin)
admin.site.register(Products, ProductsAmdin)
admin.site.register(Comments, CommentsAmdin)
admin.site.register(Subscribe, SubscribeAmdin)
