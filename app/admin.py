from django.contrib import admin
from app.models import *
from app.admin_mixin import MultiDBModelAdmin


class OrdersAmdin(admin.ModelAdmin):
    model = Orders

    list_display = ["name", "t_number", "date_created"]


class ProductsAmdin(admin.ModelAdmin):
    model = Products

    list_display = ["title", "description", "image", "is_active"]


class CommentsAmdin(admin.ModelAdmin):
    model = Comments

    list_display = ["name", "description", "photo", "date_created", "is_active", "rating"]


class SubscribeAmdin(admin.ModelAdmin):
    model = Subscribe

    list_display = ["email", "date_created"]


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


admin.site.register(Region, RegionAdmin)

title = "M3 Opt"
admin.site.site_title = title
admin.site.site_header = title
admin.site.index_title = "Админ панель M3 Opt"


admin.site.register(Orders, OrdersAmdin)
admin.site.register(Products, ProductsAmdin)
admin.site.register(Comments, CommentsAmdin)
admin.site.register(Subscribe, SubscribeAmdin)
