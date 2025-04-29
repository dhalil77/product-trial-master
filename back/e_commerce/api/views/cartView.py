from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models.cart import Cart
from ..serializers.cart import CartSerializer
from drf_yasg.utils import swagger_auto_schema


class CartView(generics.RetrieveUpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart

    @swagger_auto_schema(operation_description="Récupère le panier de l'utilisateur connecté")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Met à jour le panier de l'utilisateur connecté")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
