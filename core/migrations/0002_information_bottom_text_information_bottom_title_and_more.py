# Generated by Django 4.1.7 on 2023-04-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='bottom_text',
            field=models.TextField(default=None, verbose_name='Нижний текст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='bottom_title',
            field=models.CharField(default=None, max_length=256, verbose_name='Нижний заголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='img_1',
            field=models.FileField(default=None, upload_to='info'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='img_2',
            field=models.FileField(default=None, upload_to='info'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='img_3',
            field=models.FileField(default=None, upload_to='info'),
            preserve_default=False,
        ),
    ]
