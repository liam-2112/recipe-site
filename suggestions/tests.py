from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Suggestion
from .forms import SuggestionForm

# Create your tests here.
class TestSuggestionView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="myUsername", password="myPassword")


    def test_successful_suggestion(self):
        
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'title': 'Test', 'score': 4, 'body':'testing'}
        response = self.client.post(reverse('suggestions'), data=post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Suggestion is submitted and awaiting approval',
        response.content.decode())