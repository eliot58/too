from rest_framework import generics, views
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response


@parser_classes((MultiPartParser,))
class PostsView(views.APIView):

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER, required=False)])
    def get(self, request):
        id = request.query_params.get('id')
        if id is not None:
            serializer = PostSerializer(Post.objects.get(id=id))
        else:
            serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)



class CommentView(views.APIView):

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER)])
    def get(self, request):
        if 'id' in request.query_params:
            serializer = CommentSerializer(Comment.objects.filter(post_id=request.query_params['id']), many=True)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
