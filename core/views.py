from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product, Category
from .forms import SignUpForm

# Create your views here.


class Signup(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'core/signup.html'


class Login(LoginView):
    template_name = 'core/login.html'


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


class MyAccount(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = 'core/myaccount.html'


class EditMyAccount(LoginRequiredMixin, TemplateView):
    template_name = 'core/edit_myaccount.html'
