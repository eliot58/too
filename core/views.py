from rest_framework import generics, views
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from django.conf import settings
from django.db.models import Q

class AdsView(generics.ListAPIView):
    serializer_class = AdsSerializer
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER, required=False)])
    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        id = request.query_params.get('id')
        if id is not None:
            serializer = AdsSerializer(Ads.objects.get(id=id))
        else:
            serializer = AdsSerializer(Ads.objects.all(), many=True)
        return Response(serializer.data)


class InformationView(generics.ListAPIView):
    serializer_class = InformationSerializer
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER, required=False)])
    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        id = request.query_params.get('id')
        if id is not None:
            serializer = InformationSerializer(Information.objects.get(id=id))
        else:
            serializer = InformationSerializer(Information.objects.all(), many=True)
        return Response(serializer.data)
    

class ResolveView(generics.ListAPIView):
    serializer_class = ResolveSerializer

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER, required=False)])
    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        id = request.query_params.get('id')
        if id is not None:
            serializer = ResolveSerializer(Resolve.objects.get(id=id))
        else:
            serializer = ResolveSerializer(Resolve.objects.all(), many=True)
        return Response(serializer.data)
    
class GalleryView(generics.ListAPIView):
    serializer_class = GallerySerializer

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER, required=False)])
    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        id = request.query_params.get('id')
        if id is not None:
            serializer = GallerySerializer(Gallery.objects.get(id=id))
        else:
            serializer = GallerySerializer(Gallery.objects.all(), many=True)
        return Response(serializer.data)

class AddressView(generics.ListAPIView):
    serializer_class = AddressSerializer

    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        serializer = AddressSerializer(Address.objects.get(id=1))
        return Response(serializer.data)
    

class AgricultureView(generics.ListAPIView):
    serializer_class = AgricultureSerializer

    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        serializer = AgricultureSerializer(Agriculture.objects.get(id=1))
        return Response(serializer.data)
    
class CultureView(generics.ListAPIView):
    serializer_class = CultureSerializer

    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        serializer = CultureSerializer
        return Response(serializer.data)


class NewsView(views.APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="post id", type=openapi.TYPE_INTEGER, required=False)])
    def get(self, request, **kwargs):
        settings.LANGUAGE_CODE = kwargs["lang"]
        id = request.query_params.get('id')
        if id is not None:
            serializer = NewsSerializer(News.objects.get(id=id))
        else:
            serializer = NewsSerializer(News.objects.all(), many=True)
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

class SearchView(views.APIView):
    def get(self, request, **kwargs):
        if kwargs["cat"] == "news":
            serializer = NewsSerializer(News.objects.filter(Q(title__icontains=kwargs['q']) | Q(text__icontains=kwargs['q']) | Q(text_ky__icontains=kwargs['q']) | Q(title_ky__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "ads":
            serializer = AdsSerializer(Ads.objects.filter(Q(title__icontains=kwargs['q']) | Q(text__icontains=kwargs['q']) | Q(text_ky__icontains=kwargs['q']) | Q(title_ky__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "info":
            serializer = InformationSerializer(Information.objects.filter(Q(text__icontains=kwargs['q']) | Q(text_ky__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "resolve":
            serializer = ResolveSerializer(Resolve.objects.filter(Q(title__icontains=kwargs['q']) | Q(title_ky__icontains=kwargs['q'])), many=True)
        elif kwargs["cat"] == "gallery":
            serializer = GallerySerializer(Gallery.objects.filter(Q(description__icontains=kwargs['q']) | Q(description_ky__icontains=kwargs['q'])), many=True)
        return Response(serializer.data)