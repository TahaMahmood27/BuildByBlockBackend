from rest_framework import viewsets, status, permissions
from .models import BlockChain
from .serializers import BlockChainSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


class UpdateStatusPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PATCH' or request.method == 'PUT':
            return request.user.is_staff
        return True


class BlockChainViewSet(viewsets.ModelViewSet):
    queryset = BlockChain.objects.all()
    serializer_class = BlockChainSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [UpdateStatusPermission]

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only admin users can update the status field."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)
