# Generated by Django 4.1.7 on 2023-03-23 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='address', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адрес',
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='posts', verbose_name='Фото')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=256, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Основной текст')),
                ('text_ru', models.TextField(null=True, verbose_name='Основной текст')),
                ('text_ky', models.TextField(null=True, verbose_name='Основной текст')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Agriculture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='culture', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сельское хозяйство',
                'verbose_name_plural': 'Сельское хозяйство',
            },
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='culture', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Культура',
                'verbose_name_plural': 'Культура',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='gallery', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Галлерея',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='info', verbose_name='Фото')),
                ('text', models.TextField(verbose_name='Текст')),
                ('text_ru', models.TextField(null=True, verbose_name='Текст')),
                ('text_ky', models.TextField(null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': 'Информации',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='posts/img', verbose_name='Фото')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=256, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Основной текст')),
                ('text_ru', models.TextField(null=True, verbose_name='Основной текст')),
                ('text_ky', models.TextField(null=True, verbose_name='Основной текст')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Resolve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок заявления')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Заголовок заявления')),
                ('title_ky', models.CharField(max_length=256, null=True, verbose_name='Заголовок заявления')),
                ('file', models.FileField(upload_to='resolve', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Решение',
                'verbose_name_plural': 'Решения',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
