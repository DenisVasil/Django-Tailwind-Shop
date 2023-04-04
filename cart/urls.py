from django.urls import path
from .views import AddToCart, Cart, Checkout, Hx_menu_cart, Hx_cart_total, UpdateCart

urlpatterns = [
    path('', Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('update_cart/<int:product_id>/<str:action>/',
         UpdateCart.as_view(), name='update_cart'),
    path('add_to_cart/<int:product_id>/',
         AddToCart.as_view(), name='add_to_cart'),
    path('hx_menu_cart/', Hx_menu_cart.as_view(), name='hx_menu_cart'),
    path('hx_cart_total/', Hx_cart_total.as_view(), name='hx_cart_total'),

]
