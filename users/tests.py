from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='user_1', email='user_1@gmail.com', password='password')
        self.assertEqual(user.email, 'user_1@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='', password="password")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('superuser', 'superuser@gmail.com', 'password')
        self.assertEqual(admin_user.email, 'superuser@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='superuser', email='superuser@gmail.com', password='password', is_superuser=False)
