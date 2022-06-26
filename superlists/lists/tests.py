import re
from django.http import HttpRequest, HttpResponse
from django.urls import resolve
from lists.views import home_page
from django.test import TestCase
from django.template.loader import render_to_string

class HomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        
        
        """
        기존 코드
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        # html 마지막 부분에 공백문제를 위해 strip() 추가
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        """
