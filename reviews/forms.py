from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('score', 'title', 'body')
        widgets = {
            'score': forms.RadioSelect(attrs={'class': 'star-rating'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].choices = [(i, str(i)) for i in range(5, 0, -1)]
        self.fields['title'].widget.attrs.update({'class': 'form-input-field'})
        self.fields['body'].widget.attrs.update({'class': 'form-input-field'})
        self.fields['score'].required = False