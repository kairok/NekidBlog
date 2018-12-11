from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'created')
    #list_editable = ('user',)

admin.site.register(News, NewsAdmin)

admin.site.register(Signed)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
admin.site.register(Blog, BlogAdmin)

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)