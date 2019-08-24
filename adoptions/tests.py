from django.test import TestCase
from selenium import webdriver


class UnitTestCase(TestCase):
    
    def test_it_renders_homepage(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertTemplateUsed(response, 'home.html')

