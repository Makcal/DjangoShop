from django.http import (
    HttpResponseRedirect, HttpResponseNotFound, HttpResponseNotAllowed,
    HttpResponseBadRequest
)
from django.shortcuts import render
from django.urls import reverse

from shop.models import Product, Q


def home(request):
    return render(request, 'base.html')


def to_home(request):
    return HttpResponseRedirect(reverse('shop:home'))


def search_redirect(request):
    try:
        if request.GET['query']:
            return HttpResponseRedirect(reverse(
                'shop:search',
                args=(request.GET['query'],)
            ))

        else:
            return HttpResponseRedirect(reverse('shop:home'))

    except Exception:
        return HttpResponseRedirect(reverse('shop:home'))


def search(request, query):
    query = str(query).strip()
    if query:
        products = Product.objects.filter(
            Q(name__contains=query.lower()) | Q(desc__contains=query.lower())
        )

        return render(
            request,
            'shop/search.html',
            {
                'query': query,
                'products': products,
            }
        )

    else:
        return to_home(None)


def product(request, product_id):
    try:
        pr = Product.objects.get(id=product_id)
        return render(request, 'shop/product.html', {'product': pr})

    except Product.DoesNotExist:
        return HttpResponseNotFound()


def new_product(request):
    return render(request, 'shop/new_product.html')


def add_product(request):
    if request.method.lower() != 'post':
        return HttpResponseNotAllowed(('POST',))

    if set(request.POST.keys()) != {'name', 'desc', 'photo', 'price', 'amount', 'csrfmiddlewaretoken'}:
        return HttpResponseBadRequest()
    else:
        try:
            pr = Product(
                name=request.POST['name'],
                desc=request.POST['desc'],
                photo=request.POST['photo'],
                price=request.POST['price'],
                amount=request.POST['amount'],
            )
            pr.save()
            return render(request, 'shop/add_result.html', {'success': True})

        except Exception:
            return render(request, 'shop/add_result.html', {'success': False})
