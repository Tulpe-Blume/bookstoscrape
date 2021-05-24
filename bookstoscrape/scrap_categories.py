from pprint import pprint
import os
from urllib.parse import urljoin
import csv

from slugify import slugify

from outils import get_page
from scrap_books import main as scrap_book_main


def get_book_page_url_list(soup, url):
    """Fonction permettant de récupérer tous les liens 
    d'une categorie"""
    book_urls_list = []

    section = soup.find("div", class_="col-sm-8 col-md-9").find("section")
    book_group = section.find_all("div")[1].find("ol", class_="row")

    for book_block in book_group.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
        # dans le block, on cherche le 'a'... puis le lien
        relative_url = book_block.find("a").get("href")
        # le lien est relatif ... passage au lien absolu obligatoire
        link = urljoin(url, relative_url)
        # on ajoute le lien courant dans la liste de liens
        book_urls_list.append(link)
    return book_urls_list


def is_next_page(soup, url):
    """Fonction qui indique le lien vers une page suivante"""
    try:
        relative_next_page = soup.select_one(".next > a").get("href")
        # Le lien est relatif passage au lien absolu
        next_page = urljoin(url, relative_next_page)
        return next_page
    except AttributeError:
        return None


def get_all_books_page_url(soup, url):
    """Fonction permettant de récupérer les liens 
    des pages supplémentaires et de les rajouter à
    la liste des liens"""
    # on recupere la liste de la page courante
    book_list = get_book_page_url_list(soup, url)

    curr_url = url

    # tant qu'il existe un lien suivant...
    while is_next_page(soup, url=curr_url):
        # on suit le (lapin blanc) lien suivant
        next_url = is_next_page(soup, url=curr_url)
        # et on lui crée une soupe
        soup = get_page(next_url)

        # on récupère la liste de cette page ...
        curr_book_list = get_book_page_url_list(soup, url=next_url)

        # on ajoute la liste courrante à la liste totale(book_list)
        book_list.extend(curr_book_list)

        # On incrémente l'url
        curr_url = next_url
    # on retourne la liste complete
    return book_list


def create_csv_directory():
    """Fonction permettant de créer le repertoire
    des fichiers csv"""
    try:
        os.mkdir("csvfile")
        return ("Repertoire csv cree")
    except FileExistsError:
        return ("Le repertoire existe deja.")
    

def save_books_into_csv(csv_filename, book_info_list):
    """Fonction permettant d'enregistrer les informations des
       livres d'une catégorie dans un fichier csv"""
    with open(csv_filename, 'w', newline='') as csvfile:
        header = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                  'price_excluding_tax', 'number_available', 'product_description',
                  'category', 'review_rating', 'image_url', 'new_img_name']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for elt_dict in book_info_list:
            writer.writerow(elt_dict)
    return "The books information is saved into the CSV file"


def get_category(soup):
    """Fonction récupérant la catégorie des livres"""
    try:
        category = slugify(soup.select_one(".page-header > h1").text)
        return category
    except AttributeError:
        return None

def main(url):
    """Fonction qui scrape les livres d'une catégorie.
    Et qui retourne une liste de dictionnaires"""

    # Créer une liste vide
    all_book_info_list = []
    soup = get_page(url)
    # Récupération de la liste des urls de chaque livre
    book_url_list = get_all_books_page_url(soup, url)
    
    for book_url in book_url_list:
        # pour chaque livre, on récupère les infos (sous forme de dict)
        book_info_dict = scrap_book_main(url=book_url)
        # on ajoute la categorie
        book_info_dict['category'] = get_category(soup)
        # on ajoute le dict récupéré à la liste
        all_book_info_list.append(book_info_dict)

    # on stocke toutes ces infos dans un CSV
    # Attention création du répertoire pour les csv
    print(create_csv_directory())

    # nommer le fichier CSV en utilisant la categorie
    csv_filename = slugify(get_category(soup), max_length=80) + ".csv"

    # Faire le bon chemin pour enregistrement csv
    csv_filename = os.path.join("csvfile", csv_filename)
    
    # remplir le csv avec les infos de tous les livres
    save_books_into_csv(csv_filename, book_info_list=all_book_info_list)
    return all_book_info_list


if __name__ == "__main__":
    print("Dans scrap_categories")
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    soup = get_page(url)

    print("URL de la catégorie")
    print(url)

    print("\n\ntest de get_book_page_url_list")    
    pprint(get_book_page_url_list(soup, url=url))
    
    print("\n\ntest de is_next_page")
    print(is_next_page(soup, url=url))

    print("\n\ntest de get_all_books_page_url")
    pprint(get_all_books_page_url(soup, url=url))

    print("\n\n ici get_category")
    print(get_category(soup))
    #sys.exit()

    print("\n\ntest de main")
    pprint(main(url))


