import queue
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests

class WebScraper:
    '''
    WebScraper Class uses a multithreaded system to scrape the URL provided
    by the user and the subsequent URLs found. Threads are used in order to
    ensure that blocking requests do not impact the system.

    '''

    def __init__(self, url, max_threads):
        '''

        Parameters
        ----------
        url : String
            URL entered by the user.
        max_threads : Int
            Maximum number of threads entered by the user.

        Returns
        -------
        None.

        '''
        self.initial_url = url
        self.threads = max_threads
        self.visited_lock = Lock()
        self.web_page_visited = set() #Using set in order to avoid duplication of links
        self.web_pages_to_visit = queue.Queue()
        self.web_pages_to_visit.put(url)

    def get_host(self, url):
        '''

        Parameters
        ----------
        url : String
            URL entered by the user.

        Returns
        -------
        String
            Host extracted from the URL.

        '''
        #
        return url.split("//")[1].split("/")[0] 
    
    def get_sub_links(self, url):
        '''

        Parameters
        ----------
        url : String
            URLs to extract the links.

        Returns
        -------
        List
            List containing the sub links extracted in each webpage visited.

        '''
        sub_links=set()
        response = requests.get(url)
        if response.status_code == 200:
            #BeautifulSoup Library for parsing the HTML content from webpages
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                sub_links.add(link.get('href'))
            return list(sub_links)
        # When the response code returned from the request is not a successful
        return []
    
    def scraper(self):
        '''

        Returns
        -------
        None.

        '''
        while True:
            url = None
            try:
                url = self.web_pages_to_visit.get(timeout=20)
            except queue.Empty:
                return

            sub_urls = self.get_sub_links(url)
            for sub_url in sub_urls:
                with self.visited_lock:
                    if sub_url[0] == "/":
                        new_url = f"{url.strip('/')}/{sub_url.strip('/')}"
                        if new_url not in self.web_page_visited:
                            self.web_pages_to_visit.put(new_url)
                            self.web_page_visited.add(new_url)
                    elif self.get_host(sub_url) == self.get_host(self.initial_url) and sub_url not in self.web_page_visited:
                        self.web_pages_to_visit.put(sub_url)
                        self.web_page_visited.add(sub_url)
            

    def execute_thread(self):
        '''
        Returns
        -------
        List
            List containing all the unique URLs visited.

        '''
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for thread in range(self.threads):
                executor.submit(self.scraper)
        return list(self.web_page_visited)
