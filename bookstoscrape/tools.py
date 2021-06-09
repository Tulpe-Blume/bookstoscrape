import sys

import requests as rq
from bs4 import BeautifulSoup as BSoup


def get_page(url):
    """Fonction permettant de  vérifier si la page existe 
    et de tester s'il n'y a pas de problème
    et de retourner la soupe associée"""
    try:
        response = rq.get(url)
        response.raise_for_status()
    except rq.exceptions.ConnectionError:
        print("Il y a un problème réseau vérifier si votre réseau fonctionne.")
        sys.exit()  # Quitte le programme
    except rq.exceptions.Timeout:
        print("Votre demande a expirée.")
        sys.exit()  # Quitte le programme
    except rq.exceptions.HTTPError:
        print("La page n'est pas joignable")
        sys.exit()  # Quitte le programme
    except rq.exceptions.TooManyRedirects:
        print("Le nombre de redirections est dépassé")
        sys.exit()  # Quitte le programme
    else:
        page_soup = BSoup(response.content, "html.parser")
        return page_soup


if __name__ == "__main__":
    url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'
    print(get_page(url).prettify())
    
