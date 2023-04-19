from django import forms
from timeline.models import Comment


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

