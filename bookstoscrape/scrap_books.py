from outils import get_page
import os
from bs4 import BeautifulSoup as bs

from pprint import pprint


def get_book_info(soup):
    """Fonction permettant de récupérer les infos d'un livre
    et de les enregistrer dans un dictionnaire"""
    myBookInfos = {}
    myBookInfos["title"] = get_book_title(soup)
    myBookInfos["review_rating"] = get_book_rating(soup)
    myBookInfos["product_description"] = get_book_description(soup)
    myBookInfos["image_url"] = get_book_image_url(soup)

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
        myBookInfos[new_key] = value

    return myBookInfos


def get_book_title(soup):
    """Fonction permettant de récupérer le titre d'un livre"""
    try:
        title = soup.find("h1").text
        return title
    except:
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
    except:
        return None


def get_book_description(soup):
    """Fonction permettant de récupérer les informations de description"""
    try:
        prod_desc = soup.find_all("p")
        prod_desc = prod_desc[3].text
        return prod_desc
    except:
        return None


def get_book_table_infos(soup):
    """Fonction permettant de récupérer les informations du tableau"""
    product_info = {}
    try:
        for elt in soup.find_all("tr"):
            product_info[elt.find("th").text] = elt.find("td").text
    except:
        return None
    return product_info


def get_book_image_url(soup):
    """Fonction permettant de récupérer l'url de l'image"""
    try:
        url_image_tag = soup.find("img")
        url_image = url_image_tag['src']
        return url_image
    except:
        return None


def get_book_image(soup):
    """Fonction permettant de récupérer l'image"""
    try:
        image_url = soup.find_all("img")
    except:
        pass


def save_book_into_csv(csvfile, book_info):
    """Fonction permettant d'enregistrer les informations d'un
     livre dans un fichier csv"""
    try:
        os.mkdir("csvfile")
        return ("Repertoire csv cree")
    except FileExistsError:
        return ("Le repertoire existe deja.")
    
    


# def save_image(image):
#     pass
#     #if image exist:
#     #    continue
#     #else:
#     #    with open('image_hp_banner.png', 'wb') as image_name


# def main():
#     """??"""
#     soup = get_page('http://books.toscrape.com/catalogue/dune-dune-1_151/index.html')
#     book_info = get_book_info(soup)
#     #with open('a_category.csv') as csvfile:
#     #    save_book_into_csv(csvfile, book_info)
    
# #print(get_book_info(soup))

if __name__ == "__main__":

    url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'
    soup = get_page(url)
    # on récupère le dictionnaire
    myBookInfos = get_book_info(soup)
    myBookInfos['product_page_url'] = url
    pprint(myBookInfos)
