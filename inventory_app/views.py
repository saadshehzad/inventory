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
            supplier=supplier
        )
        return redirect("list_products")
    suppliers = Supplier.objects.all()
    return render(request, "add_product.html", {"suppliers": suppliers})

def list_products(request):
    products = Product.objects.all()
    return render(request, "list_products.html", {"products": products})

