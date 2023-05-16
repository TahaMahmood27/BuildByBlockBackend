from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlockChainViewSet

router = DefaultRouter()
router.register(r'', BlockChainViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
