from rest_framework import generics, status
from ..models.wishlist import Wishlist
from rest_framework.permissions import IsAuthenticated
from ..serializers.wishlist import WishlistSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class WishlistView(generics.RetrieveUpdateAPIView):
    """
    Vue pour gérer la liste de souhaits de l'utilisateur.
    """
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Récupérer la liste de souhaits",
        operation_description="Récupère la liste de souhaits de l'utilisateur connecté",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Liste de souhaits récupérée avec succès",
                schema=WishlistSerializer
            ),
            status.HTTP_401_UNAUTHORIZED: "Utilisateur non authentifié"
        },
        security=[{"Bearer": []}],
        tags=["wishlist"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Mettre à jour la liste de souhaits",
        operation_description="Remplace entièrement la liste de souhaits de l'utilisateur connecté",
        request_body=WishlistSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Liste de souhaits mise à jour avec succès",
                schema=WishlistSerializer
            ),
            status.HTTP_400_BAD_REQUEST: "Erreur de validation",
            status.HTTP_401_UNAUTHORIZED: "Utilisateur non authentifié"
        },
        security=[{"Bearer": []}],
        tags=["wishlist"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Mettre à jour partiellement la liste de souhaits",
        operation_description="Met à jour partiellement la liste de souhaits de l'utilisateur connecté",
        request_body=WishlistSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Liste de souhaits mise à jour avec succès",
                schema=WishlistSerializer
            ),
            status.HTTP_400_BAD_REQUEST: "Erreur de validation",
            status.HTTP_401_UNAUTHORIZED: "Utilisateur non authentifié"
        },
        security=[{"Bearer": []}],
        tags=["wishlist"]
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def get_object(self):
        """Récupère ou crée la liste de souhaits de l'utilisateur connecté"""
        wishlist, created = Wishlist.objects.get_or_create(user=self.request.user)
        return wishlist