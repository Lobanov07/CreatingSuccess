from django import forms
from django.utils import timezone

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = (
            'author',
            'is_published',)

        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'}
            ),
        }

    def clean_pub_date(self):
        pub_date = self.cleaned_data.get('pub_date')
        if pub_date:
            if timezone.is_naive(pub_date):
                pub_date = timezone.make_aware(pub_date)
            pub_date = timezone.localtime(pub_date, timezone.utc)
        return pub_date


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={'rows': '5'}
            )
        }
