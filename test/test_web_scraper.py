import unittest
from web_scraper import WebScraper
from main import get_arguments
import requests
import sys
import os


class TestWebScraper(unittest.TestCase):
    '''
    Test Class for the functions in the WebScraper Class
    '''
    def test_scraper(self):
        web_scraper = WebScraper(
            url="http://localhost:5000", max_threads=8
        )
        self.assertEqual(
            sorted(list(web_scraper.execute_thread())),
                [
                    "http://localhost:5000/test1",
                    "http://localhost:5000/test2",
                    "http://localhost:5000/test3",
                ]
            )
        self.assertNotEqual(
            sorted((web_scraper.execute_thread())),
                ["https://google.com", "http://localhost:5000/test1", "/test2", "/test3"]
            )
        
    def test_scraper_error_url(self):
        web_scraper = WebScraper(
            url="http:localhost:5000", max_threads=8
        )
        self.assertEqual(
            web_scraper.execute_thread(),
                []
            )

    def test_get_sub_links(self):
        web_scraper = WebScraper(
            url="http://localhost:5000", max_threads=8)
        sub_links = web_scraper.get_sub_links("http://localhost:5000")
        self.assertEqual(
            sorted(list(sub_links)),
                ['/test2', '/test3', 'http://google.com', 'http://localhost:5000/test1'],
            )
        self.assertNotEqual(sorted(list(sub_links)), [])

    def test_get_host(self):
        web_scraper = WebScraper("http://localhost:5000",max_threads=8)
        self.assertEqual(web_scraper.get_host("http://localhost:5000"), "localhost:5000")
    
    def test_get_arguments(self):
        self.assertEqual(get_arguments(),{'url':'https://www.monzo.com/','max_threads':os.cpu_count()+6})

if __name__ == "__main__":

    if requests.get("http://localhost:5000").status_code != 200:
        sys.exit("Please run the Test Server")

    unittest.main()
