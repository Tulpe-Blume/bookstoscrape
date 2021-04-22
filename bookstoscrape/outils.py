import requests as rq
from bs4 import BeautifulSoup as bs
import json


# brouillon code:
url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'


def get_page(url):
    """Fonction permettant de  vérifier si la page existe 
    et de tester s'il n'y a pas de problème"""
    try:
        reponse = rq.get(url)
    except rq.exceptions.ConnectionError:
        return ("Il y a un problème réseau vérifier si votre réseau fonctionne.")
    except rq.exceptions.Timeout:
        return ("Votre demande a expirée")
    except rq.exceptions.HTTPError:
        return ("La page n'est pas joingnable")
    except rq.exceptions.TooManyRedirects:
        return ("Le nombre de redirections est dépassé")
    finally:
        pass 

    return reponse

def create_soup(in_reponse):
    page_soup = bs(in_reponse.content)
    return page_soup


print("CHECKPOINT -- outils.py")
# Récuperer le contenu de la page
response = get_page(url)
# Créer la classe qui analyse le contenu de la page
page_soupe = bs(response.content)

#print(page_soupe)
print(type(page_soupe))
print("CHECKPOINT -- outils.py")


#resp = get_page(url)
#make_soup(resp)
#print(resp)
#print(resp_json)


#def product_description():
 #   """Fonction recuperant le contenu de la description produit si elle existe"""
  #  if  existe:
   #     pass
#page_soup = bs(reponse.content)


#print(page.status_code)
#print(page.headers)
