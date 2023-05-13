import re
from django.http import HttpRequest, HttpResponse
from django.urls import resolve
from lists.views import home_page
from django.test import TestCase
from django.template.loader import render_to_string
from lists.models import Item

class HomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)  # type: ignore

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

    def test_home_page_redirects_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        """
        self.assertIn('신규 작업 아이템', response.content.decode())  # type: ignore
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'}
        )
        self.assertEqual(response.content.decode(), expected_html)  # type: ignore
        
        
        기존 코드
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        # html 마지막 부분에 공백문제를 위해 strip() 추가
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        """
    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(response['location'], '/')