from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('comments/', CommentView.as_view()),
    path('ads/', AdsView.as_view()),
    path('information/', InformationView.as_view()),
    path('resolve/', ResolveView.as_view()),
    path('gallery/', GalleryView.as_view()),
    path('search/', SearchView.as_view()),
    path('address/', AddressView.as_view()),
    # path('agriculture/', AgricultureView.as_view()),
    path('culture/', CultureView.as_view()),
    path('common-info/', CommonInfoView.as_view()),
    path('faq/', FAQView.as_view()),
]