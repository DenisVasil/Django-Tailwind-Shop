from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from core.views import Frontpage, Shop, Signup, Login
from cart.views import AddToCart
from product.views import ProductDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Frontpage.as_view(), name='frontpage'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('shop/', Shop.as_view(), name='shop'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('shop/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('add_to_cart/<int:product_id>/',
         AddToCart.as_view(), name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
