import requests
from bs4 import BeautifulSoup
import time
from storage import save_data

class WebCrawler:
    BASE_URL = "https://news.ycombinator.com/"
    
    def __init__(self):
        self.entries = []

    def fetch_entries(self):
        try:
            response = requests.get(self.BASE_URL)
            if response.status_code != 200:
                return []
            soup = BeautifulSoup(response.text, 'html.parser')
            self.entries = self._parse_entries(soup)
            return self.entries
        except Exception:
            return []

    def _parse_entries(self, soup):
        try:
            titles = soup.find_all('span', class_='titleline')
            subtexts = soup.find_all('td', class_='subtext')
            entries = []
            
            if len(titles) != len(subtexts):
                return []

            for index, (title_span, subtext) in enumerate(zip(titles, subtexts)):
                title_text = title_span.find('a').get_text()

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
        except Exception:
            return []

    def crawl(self):
        try:
            fetched_entries = self.fetch_entries()
            if not fetched_entries:
                return
            
            timestamp = time.time()
            save_data(fetched_entries, timestamp, "initial_crawl")
            return fetched_entries
        except Exception:
            pass

if __name__ == "__main__":
    crawler = WebCrawler()
    crawler.crawl()
