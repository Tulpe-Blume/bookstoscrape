import requests as rq
from bs4 import BeautifulSoup as bs
import sys

# brouillon code:
url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'


def get_page(url):
    """Fonction permettant de  vérifier si la page existe 
    et de tester s'il n'y a pas de problème"""
    try:
        response = rq.get(url)
        response.raise_for_status()
    except rq.exceptions.ConnectionError:
        return ("Il y a un problème réseau vérifier si votre réseau fonctionne.")
    except rq.exceptions.Timeout:
        return ("Votre demande a expirée.")
    except rq.exceptions.HTTPError: 
        return ("La page n'est pas joignable")
    except rq.exceptions.TooManyRedirects:
        return ("Le nombre de redirections est dépassé")
    else:
        return ("La page est joignable et peut être analysée!")


def create_soup(url):
    """Fonction permettant de créer la soupe si la page existe"""
    page = rq.get(url)
    if page.ok:
        page_soup = bs(page.content.decode("utf-8", "ignore"), "html.parser")
        return (page_soup.prettify)
    else:
        sys.exit()  # Quitte le programme.


print(get_page(url))
print(create_soup(url))


# Créer la classe qui analyse le contenu de la page
#page_soupe = bs(response.content)

#print(page_soupe)
#print(type(page_soupe)