from .models import Post, post_comment
from django.forms import ModelForm, TextInput, Textarea


class Post_form(ModelForm):
    class Meta:
        model = Post
        exclude = ("user", )
        fields = ["title", "text"]
        widgets = {"title": TextInput(attrs={
            'class': "w3-padding-32",
            "placeholder": "Введите название"
        }),
            "text": Textarea(attrs={
                'class': "w3-padding-32",
                "placeholder": "Введите текст поста"
            })
        }


class Comment_form(ModelForm):
    class Meta:
        model = post_comment
        fields = ['name', 'body']



