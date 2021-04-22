import bookstoscrape.outils as tools
import os

def get_book_info(soup):
    """Fonction permettant de récupérer les infos d'un livre
    et de les enregistrer dans un dictionnaire"""
    soup = tools.create_soup(in_response)
    title_book = soup.find('h1').text
    #try:
        #creer un dico vide du nom du titre s'il n'existe pas
        # continue
    #- récuperer les infos (parser)
    for info_book in tools.create_soup.find_all('td'):
        pass
    return "hello"


def save_book_into_csv(csvfile, book_info):
    """Fonction permettant d'enregistrer les informations d'un
    livre dans un fichier csv"""
    try:
        os.mkdir("csvfile")
        print("Repertoire csv cree")
    except FileExistsError:
        print("Le repertoire existe deja.")
    
    


def save_image(image):
    #if image exist:
    #    continue
    #else:
    #    with open('image_hp_banner.png', 'wb') as image_name


def main():
    """??"""
    soup = tools.get_page(
        'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'
    )
    book_info = get_book_info(soup)
    with open('a_category.csv') as csvfile:
        save_book_into_csv(csvfile, book_info)
    


if __name__ == "__main__":
    main()
