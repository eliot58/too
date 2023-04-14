# Generated by Django 4.1.7 on 2023-04-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_information_bottom_text_information_bottom_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256, verbose_name='суроо')),
                ('answer', models.CharField(max_length=256, verbose_name='жооп')),
            ],
            options={
                'verbose_name': 'Көп берилүүчү суроо',
                'verbose_name_plural': 'Көп берилүүчү суроолор',
            },
        ),
        migrations.RemoveField(
            model_name='agriculturephoto',
            name='culture',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Дарек', 'verbose_name_plural': 'Дарек'},
        ),
        migrations.DeleteModel(
            name='Agriculture',
        ),
        migrations.DeleteModel(
            name='AgriCulturePhoto',
        ),
    ]
