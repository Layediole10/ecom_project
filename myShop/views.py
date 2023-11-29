from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    myProduct = Product.objects.all()
    myCategory = Category.objects.all()

    # la recherche de produit dans la barre de recherche
    search_elem = request.GET.get("search-elem")
    if search_elem != "" and search_elem is not None:
        myProduct = Product.objects.filter(name_prod__icontains=search_elem)
    
    # La pagination
    paginator = Paginator(myProduct, 4)
    myPaginator = request.GET.get("myPage")
    myProduct = paginator.get_page(myPaginator)

    context = {
        "myProduct" : myProduct,
    }
    return render(request, "myFirstShop/index.html", context)

# Les détails du produit
def details(request, id_prod):
    product = Product.objects.get(id=id_prod)
    return render(request, "myFirstShop/details.html", {"product": product})
    
