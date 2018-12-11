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



class Signed(models.Model):
    class Meta:
        # делает уникальным направление обмена
        unique_together = ("who", "to")

    who = models.ForeignKey(User,
            verbose_name="Автор",
            on_delete=models.CASCADE, related_name="from_who")
    to = models.ManyToManyField(User,
            verbose_name="Авторы", related_name="to_who")

    class Meta:
        verbose_name="Подписка"
        verbose_name_plural="Подписки"

    def __str__(self):
        return "{}".format(self.who)


class Blog(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=100)
    created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name="Блог"
        verbose_name_plural="Блог"

    def __str__(self):
        return "{}".format(self.user)

class News(models.Model):
    blog = models.ForeignKey(Blog, verbose_name="Блог", on_delete=models.CASCADE)
    title = models.CharField('Заголовок',max_length=100)
    text=models.TextField("Текст статьи")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    #isreaded=models.BooleanField(default=False)

    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"

    def __str__(self):
        return self.title

