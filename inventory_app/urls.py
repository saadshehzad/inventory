from django.urls import path

from . import views

urlpatterns = [
    path("add_product/", views.add_product, name="add_product"),
    path("list_products/", views.list_products, name="list_products"),
    path("add_supplier/", views.add_supplier, name="add_supplier"),
    path("list_suppliers/", views.list_suppliers, name="list_suppliers"),
    path("add_stock_movement/", views.add_stock_movement, name="add_stock_movement"),
    path("create_sales_order/", views.create_sales_order, name="create_sales_order"),
    path(
        "cancel_sales_order/<uuid:order_id>/",
        views.cancel_sales_order,
        name="cancel_sales_order",
    ),
    path("list_sales_orders/", views.list_sales_orders, name="list_sales_orders"),
    path("stock_level_check/", views.stock_level_check, name="stock_level_check"),
]
