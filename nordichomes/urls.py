from django.contrib import admin
from django.urls import path
from core.views import Frontpage, Shop
from cart.views import AddToCart
from product.views import ProductDetailView

urlpatterns = [
    path('', Frontpage.as_view(), name='frontpage'),
    path('admin/', admin.site.urls),
    path('shop/', Shop.as_view(), name='shop'),
    #path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('shop/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('add_to_cart/<int:product_id>/',
         AddToCart.as_view(), name='add_to_cart'),
]
