from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'question', 'answer_a', 'answer_b', 'answer_c')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

