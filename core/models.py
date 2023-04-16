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
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    sub_title = models.CharField(max_length=256, verbose_name='Подзаголовок')
    img = models.FileField(upload_to="info", verbose_name='Фото')
    text = models.TextField(verbose_name='Текст')

    bottom_title = models.CharField(max_length=256, verbose_name='Нижний заголовок')
    bottom_text = models.TextField(verbose_name='Нижний текст')
    img_1 = models.FileField(upload_to="info")
    img_2 = models.FileField(upload_to="info")
    img_3 = models.FileField(upload_to="info")


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Маалымат'
        verbose_name_plural = 'Маалыматтар'




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
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

class News(models.Model):
    img = models.FileField(upload_to="posts/img", verbose_name='Фото')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Основной текст')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Жаңылык'
        verbose_name_plural = 'Жаңылыктар'

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

    def save(self, *args, **kwargs):
        if len(Address.objects.all()) != 0:
            return
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Дарек'
        verbose_name_plural = 'Дарек'



# class Agriculture(models.Model):
#     description = models.TextField(verbose_name='Описание')


#     class Meta:
#         verbose_name = 'Айыл чарбасы'
#         verbose_name_plural = 'Айыл чарбасы'
    

# class AgriCulturePhoto(models.Model):
#     culture = models.ForeignKey(Agriculture, on_delete=models.CASCADE)
#     file = models.FileField(upload_to="culture")


class Culture(models.Model):
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Маданият'
        verbose_name_plural = 'Маданият'



class CulturePhoto(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    file = models.FileField(upload_to="culture")



class CommonInfo(models.Model):
    territory = models.PositiveIntegerField(verbose_name="Жалпы территориясы")
    number_of_villages = models.PositiveIntegerField(verbose_name="Айылдардын саны")
    number_of_smokes = models.PositiveIntegerField(verbose_name="Түтүндөрдүн саны")
    avg_learn = models.PositiveIntegerField(verbose_name="Атайын орто билим  берүү")
    licey = models.PositiveIntegerField(verbose_name="Лицей")
    teacher_number = models.PositiveIntegerField(verbose_name="Мугалимдердин саны")
    students_number = models.PositiveIntegerField(verbose_name="Тарбиялануучу балдардын саны")
    ogan = models.PositiveIntegerField(verbose_name="Ооган согушунун ардагерлери")
    chernobyl = models.PositiveIntegerField(verbose_name="Чернобыль кырсыгына катышкандар")
    hospital = models.PositiveIntegerField(verbose_name="Ооруканалар")
    family_medicine = models.PositiveIntegerField(verbose_name="Үй-бүлөлүк дарыгерлер")
    fap = models.PositiveIntegerField(verbose_name="ФАП")
    apteka = models.PositiveIntegerField(verbose_name="Аптекалар")
    railroad = models.PositiveIntegerField(verbose_name="Жакынкы темир жол")
    airport = models.PositiveIntegerField(verbose_name="Жакынкы аэропорт")
    district = models.PositiveIntegerField(verbose_name="Райондун борборуна чейинки аралык")
    region = models.PositiveIntegerField(verbose_name="Облустун борборуна чейинки аралык")
    sea = models.PositiveIntegerField(verbose_name="Дениз деңгээлинен бийиктиги")


    def __str__(self):
        return 'Жалпы маалыматтар'

    def save(self, *args, **kwargs):
        if len(CommonInfo.objects.all()) != 0:
            return
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Жалпы маалыматтар'
        verbose_name_plural = 'Жалпы маалыматтар'



class FAQ(models.Model):
    question = models.TextField(verbose_name="суроо")
    answer = models.TextField(verbose_name="жооп")


    class Meta:
        verbose_name = 'Көп берилүүчү суроо'
        verbose_name_plural = 'Көп берилүүчү суроолор'