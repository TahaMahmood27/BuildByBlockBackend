from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import BlogViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog', BlogViewSet)
 
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
