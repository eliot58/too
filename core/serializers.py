from rest_framework.serializers import ModelSerializer
from .models import *

class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = ['img', 'title', 'text']


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = ['title','img', 'text']


class ResolveSerializer(ModelSerializer):
    class Meta:
        model = Resolve
        fields = ['title', 'file']


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['photo', 'description']



class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['img', 'title', 'text']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['photo', 'description']

class CultureImagesSerializer(ModelSerializer):
    class Meta:
        model = CulturePhoto
        fields = '__all__'


class AgriCultureImagesSerializer(ModelSerializer):
    class Meta:
        model = AgriCulturePhoto
        fields = '__all__'

class CultureSerializer(ModelSerializer):
    images = CultureImagesSerializer(many=True, read_only = True)
    class Meta:
        model = Culture
        fields = ['description', 'images']


class AgricultureSerializer(ModelSerializer):
    images = AgriCultureImagesSerializer(many=True, read_only = True)
    class Meta:
        model = Agriculture
        fields = ['description', 'images']


class CommonInfoSerializer(ModelSerializer):
    class Meta:
        model = CommonInfo
        fields = '__all__'