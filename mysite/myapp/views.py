from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "index.html", context)


def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item': item
    }
    return render(request, "detail.html", context=context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "additem.html")


def update_item(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {'item': item}

    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/myapp/")

    return render(request, "updateitem.html", context)

def delete_item(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {'item': item}

    if request.method == "POST":
        item.delete()
        return redirect("/myapp/")

    return render(request, "deleteitem.html", context)