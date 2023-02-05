from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest (TestCase):

    def setUp(self):
        Post.objects.create(text='just a text')

    def test_post_context(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.text
        self.assertEqual(expected_object_name,'just a text')


class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text='is another text')


    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code,200)


    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)


    def test_view_users_corect_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'home.html')
