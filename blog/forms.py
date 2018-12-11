from django.forms import ModelForm
from django import forms
from .models import  *


class PostForm(ModelForm):
    class Meta:
        model = News
        fields = ('title','text','blog',)

#class DeliveryForm(ModelForm):
 #   citizenship = forms.NameModelChoiceField(label=u'Гражданство', queryset=Citizenship.objects.order_by('-name'),
  #                                     initial=Citizenship.objects.get(id=1))