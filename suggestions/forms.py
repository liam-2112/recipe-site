from .models import Suggestion
from django import forms


class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Suggestion
        fields = ('title', 'body')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-input-field'})
        self.fields['body'].widget.attrs.update({'class': 'form-input-field'})
        