from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


SITE = "https://srs.myrusakov.ru/"
visited = []


def get404(url, parent):
    response = requests.get(url)

    if response.status_code == '404':
        print(f"Битая ссылка {url=} на странице {parent=}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.select("a")
    for element in elements:
        if not element.has_attr('href'):
            continue
        else:
            href = element['href']
            if href.startswith('#') or href.startswith('tel:') or href.startswith('mailto:'):
                continue
            else:
                href = urljoin(SITE, href)
                if href not in visited and SITE in href:
                    print(href)
                    visited.append(href)
                    get404(href, url)


if __name__ == '__main__':
    get404(SITE, SITE)
