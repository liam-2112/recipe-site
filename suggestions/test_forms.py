from django.test import TestCase
from .forms import SuggestionForm


class TestSuggestionForm(TestCase):

    def test_form_is_valid(self):
        suggestion_form = SuggestionForm({'title': 'Test', 'score': 4, 'body':'testing'})
        self.assertTrue(suggestion_form.is_valid(), msg="Form is valid")