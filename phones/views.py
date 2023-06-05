from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    _sorted = request.GET.get('sort')
    # max_sorted = request.GET.get('sort=max_price')
    # name_sorted = request.GET.get('sort=name')
    template = 'catalog.html'
    if _sorted == "min_price":
        db = Phone.objects.all().order_by('price')
    elif _sorted == "max_price":
         db = Phone.objects.all().order_by('-price')
    elif _sorted == 'name':
        db = Phone.objects.all().order_by('name')

    else:
        db = Phone.objects.all()

    context = {
        "phones": db,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    db = Phone.objects.get(slug=slug)
    context = {
        "phone": db,
    }
    print(db)
    return render(request, template, context)

