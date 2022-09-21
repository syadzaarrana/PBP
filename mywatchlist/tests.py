from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_mywatchlist_url(self):
        response = self.client.get(reverse('mywatchlist:show_watchlist'))
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_html_url(self):
        response = self.client.get(reverse('mywatchlist:show_html'))
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_xml_url(self):
        response = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_json_url(self):
        response = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code,200)