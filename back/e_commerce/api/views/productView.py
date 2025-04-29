
from ..models.product import Product
from rest_framework import viewsets, mixins 
from drf_yasg.utils import swagger_auto_schema
from ..serializers.product import ProductSerializer
from ..permission import IsAdminEmail
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class ProductViewSet( mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return [IsAuthenticated()]
    #     return [IsAuthenticated(), IsAdminEmail()]  
    

    @swagger_auto_schema(operation_description="Créer un nouveau produit")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Lister tous les produits")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Détails d’un produit")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Mettre à jour un produit partiellement")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Supprimer un produit")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

