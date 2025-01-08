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

def add_supplier(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        
        Supplier.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        return redirect("list_suppliers")
    return render(request, "add_supplier.html")

def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "list_suppliers.html", {"suppliers": suppliers})
