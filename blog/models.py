from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.
#User=get_user_model()
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    issigned = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Clients(models.Model):
    user = models.ForeignKey(User,
            verbose_name="Автор",
            on_delete=models.CASCADE)

    class Meta:
        verbose_name="Автор"
        verbose_name_plural="Авторы"

    def __str__(self):
        return self.user

class News(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    title = models.CharField('Заголовок',max_length=100)
    text=models.TextField("Текст статьи")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    isreaded=models.BooleanField(default=False)

    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"

    def __str__(self):
        return self.title