from django.db import models

class Post(models.Model):
    img = models.FileField(upload_to="posts/img", verbose_name='Фото к посту')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержание поста')


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    text = models.TextField()


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'