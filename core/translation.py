from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')



@register(Ads)
class AdsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Information)
class InformationTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Resolve)
class ResolveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('description',)



@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Agriculture)
class AgricultureTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Culture)
class CultureTranslationOptions(TranslationOptions):
    fields = ('description',)