from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'
    password = 'Superpassword'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects
        self.assertEqual(users.all().count(), 1)
        self.assertEqual(users.first().username, self.username)
        self.assertEqual(users.first().email, self.email)
