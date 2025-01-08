from django.contrib import admin
from .models import Supplier, Product, SalesOrder, StockMovement

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'supplier', 'created_at', 'updated_at')
    search_fields = ('name', 'category')
    list_filter = ('category',)

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'sale_date', 'status', 'created_at', 'updated_at')
    search_fields = ('product__name',)
    list_filter = ('status', 'sale_date')

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'movement_type', 'movement_date', 'notes', 'created_at', 'updated_at')
    search_fields = ('product__name', 'movement_type')
    list_filter = ('movement_type', 'movement_date')
