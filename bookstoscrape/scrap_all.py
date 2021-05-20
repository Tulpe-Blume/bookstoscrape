from pprint import pprint
from urllib.parse import urljoin

from bs4 import BeautifulSoup as BSoup

from outils import get_page
from scrap_books import get_book_info

def get_categories_url(soup, url):
    """Fonction permettant de récupérer tous 
    les liens des catégories"""
    categories_urls_list = []
    categories_group = soup.select_one(".nav-list  ul")
    
    for categories_block in categories_group.find_all("li"):
        relative_url = categories_block.find("a").get("href")
        # Le lien est relatif ... passage au lien absolu obligatoire
        link = urljoin(url, relative_url)
        # On ajoute le lien courant dans la liste de liens
        categories_urls_list.append(link)
    
    return categories_urls_list


def main():
    print("dans scrap_all.py")
    url = "http://books.toscrape.com/index.html"
    soup = get_page(url)
    pprint(get_categories_url(soup, url))

if __name__ == "__main__":
    main()

