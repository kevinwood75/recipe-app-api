from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setup(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            
        )
