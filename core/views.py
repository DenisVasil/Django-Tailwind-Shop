from django.shortcuts import render
from django.db.models import Q
from django.views import View
from django.views.generic.list import ListView
from product.models import Product, Category
# Create your views here.


class Frontpage(ListView):
    queryset = Product.objects.all()[:8]
    template_name = 'core/frontpage.html'
    context_object_name = 'products'


class Shop(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()
        active_category = request.GET.get('category', '')
        if active_category:
            products = products.filter(category__slug=active_category)

        query = request.GET.get('query', '')

        if query:
            products = products.filter(
                Q(name__icontains=query) | Q(description__icontains=query))
        context = {'products': products,
                   'categories': categories,
                   'active_categoty': active_category}
        return render(request, 'core/shop.html', context)
