
from .views import * 
from .models import *
from .views.cartView import *
from .views.wishlistView import *
from .views.authenticate import *
from django.urls import path, include
from .views.productView import ProductViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
    path('account', RegisterView.as_view(), name='register'),
    path('token', LoginView.as_view(), name='login'),
    path('cart/', CartView.as_view(), name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]



