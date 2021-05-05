from django.db import models


class Products(models.Model):

    title = models.CharField("Заголовок", max_length=255, blank=True)
    description = models.TextField("Описание", max_length=5000, blank=True)
    image = models.ImageField("Изображение", upload_to="product_image/", blank=True)
    is_active = models.BooleanField("Активно на странице", default=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Orders(models.Model):

    name = models.CharField("Имя", max_length=255, blank=True)
    t_number = models.CharField("Номер телефона", max_length=20, blank=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Comments(models.Model):

    name = models.CharField("Имя", max_length=255, blank=True)
    description = models.TextField("Описание", max_length=10000, blank=True)
    photo = models.ImageField("Изображение", upload_to="comments_photo/", blank=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активно на странице", default=False)
    rating = models.IntegerField("Оценка")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Subscribe(models.Model):

    email = models.CharField("Почта", max_length=500, blank=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"


class Region(models.Model):

    name = models.CharField("Наименование", max_length=100, blank=True, unique=True)
    is_active = models.BooleanField("Активно на странице", default=False)
    descripton = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"

    def __str__(self):
        return f"{self.name}"


class Stock(models.Model):

    address = models.CharField("Адресс", max_length=1000, blank=True)
    map_link = models.TextField("Ссылка на карту", blank=True)
    phone = models.CharField("Номер телефона", max_length=25, blank=True)
    region = models.ForeignKey(
        Region, verbose_name="Область", related_name="stock", on_delete=models.CASCADE, to_field="descripton"
    )
    is_active = models.BooleanField("Активно на странице", default=False, blank=True)

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"

    def __str__(self):
        return f"Область: {self.region.name}"


class Port(models.Model):

    map_link = models.TextField("Ссылка на карту", blank=True)
    address = models.CharField("Адресс", max_length=1000, blank=True)
    phone = models.CharField("Номер телефона", max_length=25, blank=True)
    region = models.ForeignKey(
        Region, verbose_name="Область", related_name="port", on_delete=models.CASCADE, to_field="descripton"
    )
    is_active = models.BooleanField("Активно на странице", default=False, blank=True)

    class Meta:
        verbose_name = "Порт"
        verbose_name_plural = "Порты"

    def __str__(self):
        return f"Область: {self.region.name}"





















