from django.forms import ModelForm

from .models import  *

class PostForm(ModelForm):
    class Meta:
        model = News
        fields = ('title','text',)