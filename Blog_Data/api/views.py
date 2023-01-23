from rest_framework.decorators import api_view
from rest_framework.response import Response
from Blog_Data.models import Blog
from .serializers import BlogSerializer

@api_view(['GET'])
def getroutes(request):
    routes = [
        'GET /api',
        "GET /api/rooms"
    ]
    return Response(routes)

@api_view(['GET'])
def getBlog(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

# Create your views here.
