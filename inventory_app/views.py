from datetime import date
from decimal import Decimal

from bson import Decimal128
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, SalesOrder, StockMovement, Supplier


def add_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST.get("description", "")
        category = request.POST["category"]
        price = float(request.POST["price"])
        stock_quantity = int(request.POST["stock_quantity"])
        supplier_id = request.POST["supplier_id"]
        supplier = Supplier.objects.get(id=supplier_id)

        Product.objects.create(
            name=name,
            description=description,
            category=category,
            price=price,
            stock_quantity=stock_quantity,
            supplier=supplier,
        )
        return redirect("list_products")
    suppliers = Supplier.objects.all()
    return render(request, "add_product.html", {"suppliers": suppliers})


def list_products(request):
    products = Product.objects.all()
    return render(request, "list_products.html", {"products": products})


def add_supplier(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        Supplier.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect("list_suppliers")
    return render(request, "add_supplier.html")


def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "list_suppliers.html", {"suppliers": suppliers})


def add_stock_movement(request):
    if request.method == "POST":
        product_id = request.POST["product_id"]
        quantity = int(request.POST["quantity"])
        movement_type = request.POST["movement_type"]
        notes = request.POST.get("notes", "")
        product = Product.objects.get(id=product_id)

        if movement_type == "In":
            product.stock_quantity += quantity
        elif movement_type == "Out" and product.stock_quantity >= quantity:
            product.stock_quantity -= quantity
        else:
            return JsonResponse({"error": "Invalid stock movement"}, status=400)

        product.save()

        StockMovement.objects.create(
            product=product,
            quantity=quantity,
            movement_type=movement_type,
            movement_date=date.today(),
            notes=notes,
        )
        return redirect("list_products")
    products = Product.objects.all()
    return render(request, "add_stock_movement.html", {"products": products})


def create_sales_order(request):
    if request.method == "POST":
        product_id = request.POST["product_id"]
        quantity = int(request.POST["quantity"])
        product = Product.objects.get(id=product_id)

        if product.stock_quantity < quantity:
            return JsonResponse({"error": "Insufficient stock"}, status=400)

        total_price = product.price * quantity
        SalesOrder.objects.create(
            product=product,
            quantity=quantity,
            total_price=total_price,
            sale_date=date.today(),
            status="Pending",
        )

        product.stock_quantity -= quantity
        product.save()
        return redirect("list_sales_orders")
    products = Product.objects.all()
    return render(request, "create_sales_order.html", {"products": products})


def cancel_sales_order(request, order_id):
    order = get_object_or_404(SalesOrder, id=order_id)
    if order.status == "Pending":
        order.status = "Cancelled"
        order.total_price = order.total_price.to_decimal()
        order.save()

        product = order.product
        order.total_price = Decimal(order.total_price)
        product.save()

    return redirect("list_sales_orders")


def list_sales_orders(request):
    orders = SalesOrder.objects.all()
    return render(request, "list_sales_orders.html", {"orders": orders})


def stock_level_check(request):
    products = Product.objects.all()
    return render(request, "stock_level.html", {"products": products})
