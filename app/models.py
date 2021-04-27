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

    name = models.CharField("Заголовок", max_length=255, blank=True)
    t_number = models.CharField("Заголовок", max_length=20, blank=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Comments(models.Model):

    name = models.CharField("Заголовок", max_length=255, blank=True)
    description = models.TextField("Описание", max_length=10000, blank=True)
    photo = models.ImageField("Изображение", upload_to="comments_photo/", blank=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активно на странице", default=False)
    rating = models.IntegerField("Оценка")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
