from pprint import pprint
from urllib.parse import urljoin

from bookstoscrape.tools import get_page
from bookstoscrape.scrap_categories import main as scrap_categories_main


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

    # on récupère la liste des urls de toutes les categories
    all_categories_url_list = get_categories_url(soup, url)

    # pour chacune, on appelle scrap_categories (qui va faire tout...)
    for category_url in all_categories_url_list:
        scrap_categories_main(category_url)


if __name__ == "__main__":
    print(main())

