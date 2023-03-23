from rest_framework.serializers import ModelSerializer
from .models import *

class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = ['img', 'title', 'text']


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = ['img', 'text']


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


class CultureSerializer(ModelSerializer):
    class Meta:
        model = Culture
        fields = ['photo', 'description']


class AgricultureSerializer(ModelSerializer):
    class Meta:
        model = Agriculture
        fields = ['photo', 'description']