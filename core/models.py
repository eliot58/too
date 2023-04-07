from django.db import models


class Ads(models.Model):
    img = models.FileField(upload_to="posts", verbose_name='Фото')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Основной текст')


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Жарыя'
        verbose_name_plural = 'Жарыялар'


class Information(models.Model):
    img = models.FileField(upload_to="info", verbose_name='Фото')
    text = models.TextField(verbose_name='Текст')


    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'Малымат'
        verbose_name_plural = 'Малыматтар'




class Resolve(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок заявления')
    file = models.FileField(upload_to="resolve",verbose_name='Документ')

    class Meta:
        verbose_name = 'Токтом'
        verbose_name_plural = 'Токтомдор'



class Gallery(models.Model):
    photo = models.FileField(upload_to='gallery', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'

class News(models.Model):
    img = models.FileField(upload_to="posts/img", verbose_name='Фото')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Основной текст')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Жанылык'
        verbose_name_plural = 'Жанылыктар'

class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость')
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Address(models.Model):
    photo = models.FileField(upload_to='address', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Дарег'
        verbose_name_plural = 'Дарег'



class Agriculture(models.Model):
    description = models.TextField(verbose_name='Описание')


    class Meta:
        verbose_name = 'Айыл чарбасы'
        verbose_name_plural = 'Айыл чарбасы'
    

class AgriCulturePhoto(models.Model):
    culture = models.ForeignKey(Agriculture, on_delete=models.CASCADE)
    file = models.FileField(upload_to="culture")


class Culture(models.Model):
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Маданият'
        verbose_name_plural = 'Маданият'



class CulturePhoto(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    file = models.FileField(upload_to="culture")