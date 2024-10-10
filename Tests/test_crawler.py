import requests
from bs4 import BeautifulSoup
import re
import time
from storage import save_data

class WebCrawler:
    BASE_URL = "https://news.ycombinator.com/"
    
    def __init__(self):
        self.entries = []

    def fetch_entries(self):
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.entries = self._parse_entries(soup)
        return self.entries

    def _parse_entries(self, soup):
        titles = soup.find_all('a', class_='storylink')
        subtexts = soup.find_all('td', class_='subtext')
        entries = []
        for index, (title, subtext) in enumerate(zip(titles, subtexts)):
            title_text = title.get_text()
            points = subtext.find('span', class_='score')
            points = int(points.get_text().split()[0]) if points else 0
            comments = subtext.find_all('a')[-1].get_text()
            comments = int(comments.split()[0]) if 'comment' in comments else 0
            entries.append({
                'number': index + 1,
                'title': title_text,
                'points': points,
                'comments': comments
            })
        return entries[:30]

    def crawl(self):
        fetched_entries = self.fetch_entries()
        timestamp = time.time()
        save_data(fetched_entries, timestamp, "initial_crawl")
        return fetched_entries
