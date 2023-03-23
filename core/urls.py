from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^(?P<lang>(ru|ky))/news/$', NewsView.as_view()),
    path('comments/', CommentView.as_view()),
    re_path(r'^(?P<lang>(ru|ky))/ads/$', AdsView.as_view()),
    re_path(r'^(?P<lang>(ru|ky))/information/$', InformationView.as_view()),
    re_path(r'^(?P<lang>(ru|ky))/resolve/$', ResolveView.as_view()),
    re_path(r'^(?P<lang>(ru|ky))/gallery/$', GalleryView.as_view()),
    re_path(r'^search/(?P<cat>(ads|news|info|resolve|gallery))/<str:q>/$', SearchView.as_view()),
    re_path(r'^(?P<lang>(ru|ky))/address/$', AddressView.as_view()),
    re_path(r'^(?P<lang>(ru|ky))/agriculture/$', AgricultureView.as_view()),
    re_path(r'^(?P<lang>(ru|ky))/culture/$', CultureView.as_view()),
]