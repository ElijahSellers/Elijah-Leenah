from django import forms
from leblog.models import Post
from django.conf import settings

class PostArticle(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
