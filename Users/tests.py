from django.test import TestCase
from Users.models import CustomUser


class AuthTestCase(TestCase):
    def setUp(self):
        self.u = CustomUser.objects.create_user('admin@admin.com', '12345')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='admin@admin.com', password='12345')
