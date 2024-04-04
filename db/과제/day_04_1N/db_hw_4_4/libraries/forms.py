from django import forms
from .models import Book, Review


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ('title', 'content',)
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)