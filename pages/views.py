from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages  
from .forms import ProductForm  

class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 499.99},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999.99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 49.99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 19.99}
    ]

class HomePageView(View):
    template_name = "pages/home.html"

    def get(self, request):
        return render(request, self.template_name, {"title": "Home"})

class AboutPageView(View):
    template_name = "pages/about.html"

    def get(self, request):
        return render(request, self.template_name, {"title": "About Us"})

class ProductIndexView(View):
    template_name = "products/index.html"

    def get(self, request):
        viewData = {
            "title": "Products - Online Store",
            "products": Product.products
        }
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = "products/show.html"

    def get(self, request, id):
        product = next((p for p in Product.products if p["id"] == str(id)), None)
        if not product:
            return HttpResponseRedirect("/")  
        return render(request, self.template_name, {"title": product["name"], "product": product})

class ProductCreateView(View):
    template_name = "products/create.html"

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {"title": "Create Product", "form": form})

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            new_product = {
                "id": str(len(Product.products) + 1),
                "name": form.cleaned_data["name"],
                "price": form.cleaned_data["price"],
                "description": form.cleaned_data.get("description", "")  
            }
            Product.products.append(new_product)

            messages.success(request, "Product created!")  
            return redirect("product_success")  
        
        return render(request, self.template_name, {"title": "Create Product", "form": form})

# Vista para mostrar success.html
def product_success(request):
    return render(request, "products/success.html")
