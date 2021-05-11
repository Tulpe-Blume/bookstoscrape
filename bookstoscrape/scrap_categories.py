from pprint import pprint
import os
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as BSoup

from outils import get_page
from scrap_books import get_book_info


def get_book_page_url(soup, url):
    """Fonction permettant de récupérer tous les liens 
    d'une categorie"""
    book_link_list = []

    section = soup.find("div", class_="col-sm-8 col-md-9").find("section")
    book_group = section.find_all("div")[1].find("ol", class_="row")

    for book_block in book_group.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
        # dans le block, on cherche le 'a'... puis le lien
        relative_url = book_block.find("a").get("href")
        # le lien est relatif ... passage au lien absolu obligatoire
        link = urljoin(url, relative_url)
        # on ajoute le lien courant dans la liste de liens
        book_link_list.append(link)
    return book_link_list


# def is_next_page(soup):
#     """Fonction indiquant s'il existe une page suivante"""
#     next_page = 
#     return


# def get_next_page(soup):
#     """Fonction permettant d'aller à la page suivante"""
#     return next_url


# def get_all_books_page_url(soup, url):
#     # on recupere la liste de la page courante
#     book_list = get_book_page_url(soup, url)

#     # tant qu'il existe un lien suivant...
#     while is_next_page():

#         # on suit le (lapin blanc) lien suivant
#         next_url = get_next_page(soup)
#         # et on lui crée une soupe
#         next_soup = get_page(next_url)
#         # on récupère la liste de cette page ...
#         curr_book_list = get_book_page_url(next_soup, next_url)
#         # on ajoute la liste courrante à la liste précédente
#         for curr_book in curr_book_list:
#             book_list.append(curr_book)

#     # on retourne la liste complete
#     return


def create_csv_directory():
    """Fonction permettant de créer le repertoire
    des fichiers csv"""
    try:
        os.mkdir("csvfile")
        return ("Repertoire csv cree")
    except FileExistsError:
        return ("Le repertoire existe deja.")


def save_book_into_csv(csvfile, book_info):
    """Fonction permettant d'enregistrer les informations d'un
     livre dans un fichier csv"""
    pass
    
    


def main():
    """Doc"""
    print("Dans scrap_categories")

    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    soup = get_page(url)
    pprint(get_book_page_url(soup, url))

    # Attention création du répertoire pour les csv
    print(create_csv_directory())

if __name__ == "__main__":
    main()
