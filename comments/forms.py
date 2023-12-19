from django import forms
from .models import Comment

RATINGS = [(1, 'Very bad'),
           (2, 'Bad'),
           (3, 'Ok'),
           (4, 'Good'),
           (5, 'Great!')]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'rating')

    rating = forms.ChoiceField(label='What will you rate this product?',
                               choices=RATINGS,
                               widget=forms.RadioSelect)
