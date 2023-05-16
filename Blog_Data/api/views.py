from rest_framework.decorators import api_view
from rest_framework.response import Response
from Blog_Data.models import Blog
from .serializers import BlogSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Create your views here.
