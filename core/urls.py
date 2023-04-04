from django.urls import path

from .views import Frontpage, Shop, Signup, Login, MyAccount, EditMyAccount
from product.views import ProductDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Frontpage.as_view(), name='frontpage'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('myaccount', MyAccount.as_view(), name='myaccount'),
    path('myaccount/edit', EditMyAccount.as_view(), name='edit_myaccount'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('shop/', Shop.as_view(), name='shop'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('shop/<slug:slug>/', ProductDetailView.as_view(), name='product'),
]
