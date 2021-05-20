from pprint import pprint
import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup as BSoup
import requests as rq
from slugify import slugify

from outils import get_page


def get_book_info(soup, url):
    """Fonction permettant de récupérer les infos d'un livre
    et de les enregistrer dans un dictionnaire"""
    my_book_infos = {}
    my_book_infos["title"] = get_book_title(soup)
    my_book_infos["review_rating"] = get_book_rating(soup)
    my_book_infos["product_description"] = get_book_description(soup)
    my_book_infos["image_url"] = get_book_image_url(soup, url)

    tmp_dict = get_book_table_infos(soup)
    for key, value in tmp_dict.items():
        if key == "UPC":
            new_key = "universal_product_code"
        elif key == "Price (excl. tax)":
            new_key = "price_excluding_tax"
        elif key == "Price (incl. tax)":
            new_key = "price_including_tax"
        elif key == "Availability":
            new_key = "number_available"
        else:
            continue
        my_book_infos[new_key] = value

    return my_book_infos


def get_book_title(soup):
    """Fonction permettant de récupérer le titre d'un livre"""
    try:
        title = soup.find("h1").text
        return title
    except AttributeError:
        return None


def get_book_rating(soup):
    """Fonction permettant de récupérer la notation"""
    try:
        rating = soup.find("div", class_= "col-sm-6 product_main")
        if rating.find("p", class_ = "star-rating One"):
            ratings = 1
        elif rating.find("p", class_ = "star-rating Two"):
            ratings = 2
        elif rating.find("p", class_ = "star-rating Three"):
            ratings = 3
        elif rating.find("p", class_ = "star-rating Four"):
            ratings = 4
        elif rating.find("p", class_ = "star-rating Five"):
            ratings = 5
        else:
            ratings = None
        return ratings 
    except AttributeError:
        return None


def get_book_description(soup):
    """Fonction permettant de récupérer les informations de description"""
    try:
        prod_desc = soup.select_one(".product_page > p").text
        return prod_desc
    except AttributeError:
        return None


def get_book_table_infos(soup):
    """Fonction permettant de récupérer les informations du tableau"""
    product_info = {}

    for elt in soup.find_all("tr"):
        product_info[elt.find("th").text] = elt.find("td").text
    
    return product_info


def get_book_image_url(soup, url):
    """Fonction permettant de récupérer l'url de l'image"""
    try:
        url_image_tag = soup.find("img")
        relative_url_image = url_image_tag['src']
        url_image = urljoin(url, relative_url_image)
        return url_image
    except TypeError:
        return None


def get_book_image(soup, url):
    """Fonction permettant de récupérer l'image"""
    response = rq.get(get_book_image_url(soup, url))

    if response.ok:
        return response.content
    else:
        return None


def create_image_directory():
    """Fonction permettant de créer le repertoire
    images"""
    try:
        os.mkdir("imgs")
        return "Le repertoire imgs a été créé"
    except FileExistsError:
        return "Le repertoire imgs existe déjà."


def save_image(img_name, soup, url):
    """Fonction permettant d'enregistrer l'image
    dans un dossier"""
    with open(img_name, 'wb') as image:
        image.write(get_book_image(soup, url))
    return "image sauvegardée"


def main(url):
    """Fonction qui scrape un livre"""
    soup = get_page(url)
    # on récupère le dictionnaire
    my_book_infos = get_book_info(soup, url)
    my_book_infos['product_page_url'] = url
    
    print(get_book_image_url(soup, url))
    
    # Attention création du répertoire pour les images
    print(create_image_directory())

    # Renommage de l'image avec son "titre" et sauvegarde dans le répertoire imgs
    # On capture le titre dans une variable
    img_title = my_book_infos["title"]
    # On nettoie et tronque le titre à une longueur de 80
    clean_img_name = slugify(img_title, max_length=80) + ".jpg"
    # On sauvegarde dans my_book_infos le nouveau titre
    my_book_infos['new_img_name'] = clean_img_name
    # On renomme l'image et on fait la sauvegarde
    img_name = os.path.join("imgs", clean_img_name)
    print(save_image(img_name, soup, url))

    return my_book_infos
    

if __name__ == "__main__":

    url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'

    # Appel de la fonction main
    pprint(main(url))
