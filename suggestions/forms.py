from .models import Suggestion
from django import forms


class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Suggestion
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