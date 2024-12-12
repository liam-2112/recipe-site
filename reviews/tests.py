from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Review
from .forms import ReviewForm

# Create your tests here.
class TestReviewView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="myUsername", password="myPassword")


    def test_successful_review(self):
        
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'title': 'Test', 'score': 4, 'body':'testing'}
        response = self.client.post(reverse('reviews'), data=post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Review is submitted and awaiting approval',
        response.content.decode())