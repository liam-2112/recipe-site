from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = ReviewForm({'title': 'Test', 'score': 4, 'body':'testing'})
        self.assertTrue(review_form.is_valid(), msg="Form is valid")