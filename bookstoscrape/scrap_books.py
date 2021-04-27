from outils import get_page
import os
from bs4 import BeautifulSoup as bs


url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'
soup = get_page(url)


def get_book_info(soup):
    """Fonction permettant de récupérer les infos d'un livre
    et de les enregistrer dans un dictionnaire"""
    myBookInfos = {}    
    books = soup.find_all("article")
    for book in books:
        book_infos = get_title_book(soup), get_rating(soup),
        get_product_description(soup), get_product_infos (soup)
        myBookInfos.append(book_infos)
    return myBookInfos    


def get_title_book(soup):
    """Fonction permettant de récupérer le titre d'un livre"""
    try:
        title = soup.find("h1").text
        return title
    finally:
        continue


def get_rating(soup):
    """Fonction permettant de récupérer la notation"""
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
        continue 
    return ratings 


def get_product_description(soup):
    """Fonction permettant de récupérer les informations de description"""
    try:
        prod_desc = soup.find_all("p")
        prod_desc = prod_desc[3].text
        return prod_desc
    finally:
        continue


def get_product_infos(soup):
    """Fonction permettant de récupérer les informations du tableau"""
    try:
        for elt in soup.find_all("td"):
            pass
        #print("{}".format(elt.text))


def get_image(soup):
    """Fonction permettant de récupérer l'image"""
    try:
        image = soup.find_all("img")
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

# if __name__ == "__main__":
#     main()

# #soup = tools.create_soup(url)
# #soupe = soup.find("h1").text
# #print(soupe)