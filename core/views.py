from rest_framework import generics, views
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN
)

class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10

class CultureClass:

    def __init__(self, description, images):
        self.description = description
        self.images = images

class AdsView(generics.ListAPIView):
    serializer_class = AdsSerializer
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        id = self.request.query_params.get('id')
        if id is not None:
            data = Ads.objects.filter(id=id)
        else:
            data = Ads.objects.all()
        return data


class InformationView(generics.ListAPIView):
    serializer_class = InformationSerializer
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        id = self.request.query_params.get('id')
        if id is not None:
            data = Information.objects.filter(id=id)
        else:
            data = Information.objects.all()
        return data
    

class ResolveView(generics.ListAPIView):
    serializer_class = ResolveSerializer
    def get_queryset(self, *args, **kwargs):
        id = self.request.query_params.get('id')
        if id is not None:
            data = Resolve.objects.filter(id=id)
        else:
            data = Resolve.objects.all()
        return data
    
class GalleryView(generics.ListAPIView):
    serializer_class = GallerySerializer
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        id = self.request.query_params.get('id')
        if id is not None:
            data = Gallery.objects.filter(id=id)
        else:
            data = Gallery.objects.all()
        return data

class AddressView(generics.ListAPIView):
    serializer_class = AddressSerializer
    def get(self, request, **kwargs):
        serializer = AddressSerializer(Address.objects.get(id=1))
        return Response(serializer.data)
    

class CommonInfoView(generics.ListAPIView):
    serializer_class = CommonInfoSerializer
    def get(self, request, **kwargs):
        serializer = CommonInfoSerializer(CommonInfo.objects.get(id=1))
        return Response(serializer.data)
    

class FAQView(generics.ListAPIView):
    serializer_class = FAQSerializer
    def get(self, request, **kwargs):
        serializer = FAQSerializer(FAQ.objects.all(), many=True)
        return Response(serializer.data)
    

# class AgricultureView(views.APIView):
#     def get(self, request):
#         serializer = AgricultureSerializer(CultureClass(description = Agriculture.objects.get(id=1).description, images=AgriCulturePhoto.objects.all()))
#         return Response(serializer.data)

    
class CultureView(views.APIView):
    def get(self, request):
        serializer = CultureSerializer(CultureClass(description = Culture.objects.get(id=1).description, images=CulturePhoto.objects.all()))
        return Response(serializer.data)

class NewsView(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        id = self.request.query_params.get('id')
        if id is not None:
            data = News.objects.filter(id=id)
        else:
            data = News.objects.all()
        return data



class CommentView(views.APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER)])
    def get(self, request):
        if 'id' in request.query_params:
            serializer = CommentSerializer(Comment.objects.filter(post_id=request.query_params['id']), many=True)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class SearchView(views.APIView):
    def get(self, request, **kwargs):
        if kwargs["cat"] == "news":
            serializer = NewsSerializer(News.objects.filter(Q(title__icontains=kwargs['q']) | Q(text__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "ads":
            serializer = AdsSerializer(Ads.objects.filter(Q(title__icontains=kwargs['q']) | Q(text__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "info":
            serializer = InformationSerializer(Information.objects.filter(Q(text__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "resolve":
            serializer = ResolveSerializer(Resolve.objects.filter(Q(title__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "gallery":
            serializer = GallerySerializer(Gallery.objects.filter(Q(description__icontains=kwargs['q'])), many=True)
        return Response(serializer.data)