from outils import get_page
import os
from bs4 import BeautifulSoup as bs


url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'

def get_book_info(soup):
    """Fonction permettant de récupérer les infos d'un livre
    et de les enregistrer dans un dictionnaire"""
    myDico = {}    
    soup = get_page(url)

    print(soup.head)

    title = soup.find('title').text
    print(title)

    #- récuperer les infos (parser)
    for elt in soup.find_all("td"):
        print("{}".format(elt.text))
    
     #   return (elt)
    return "hello"


def save_book_into_csv(csvfile, book_info):
    """Fonction permettant d'enregistrer les informations d'un
    livre dans un fichier csv"""
    try:
        os.mkdir("csvfile")
        return ("Repertoire csv cree")
    except FileExistsError:
        return ("Le repertoire existe deja.")
    
    


def save_image(image):
    pass
    #if image exist:
    #    continue
    #else:
    #    with open('image_hp_banner.png', 'wb') as image_name


def main():
    """??"""
    soup = get_page('http://books.toscrape.com/catalogue/dune-dune-1_151/index.html')
    book_info = get_book_info(soup)
    #with open('a_category.csv') as csvfile:
    #    save_book_into_csv(csvfile, book_info)
    
#print(get_book_info(soup))

if __name__ == "__main__":
    main()

#soup = tools.create_soup(url)
#soupe = soup.find("h1").text
#print(soupe)