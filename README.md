# Projet2 d'OpenClassrooms: Books.toscrape

## 1/Présentation

C'est un programme qui permet de scraper les informations du site [books.toscrape.com](http://books.toscrape.com/). Il récupère pour chaque livre les informations suivantes:
- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

Ces informations sont enregistrées dans un fichier CSV (un pour chaque catégorie). Les images, convertures des livres sont également récupérées dans un dossier "imgs". 

## 2/Installation

Afin de pouvoir le tester chez vous, le programme nécessite des prérequis. Il est aussi recommandé de l'installer dans un environnement virtuel, voir procédure ci-dessous.

### Prérequis

Le programme télécharge des images, des informations, par conséquent, il est important d'avoir un minimum de 50Mo de mémoire disponible sur votre disque dur ou SSD.

Ce programme utilise python3.8.8, il est nécessaire qu'il soit installé sur votre ordinateur. Pour télécharger python c'est [ici](https://www.python.org/downloads/) !

### Environnement virtuel

**Pour Windows:**

Création:
	
	python -m venv env
Activation:
	
	env/Scripts/activate.bat
	
**Linux/macOS:**

Création:
	
	python -m venv env
Activation:
	
	source env/bin/activate

### Installation des Bibliothèques

Pour que le programme fonctionne il faut aussi installer les bibliothèques supplémentaires. On utilise le fichier requirements.txt, dans lequel elles sont déjà listées:
	
	pip install -r requirements.txt

## 3/Lancer le programme

Pour ce faire, lancer le programme dans un terminal: 

	python3 -m bookstoscrape
	
Le programme va alors sauvegarder toutes les convertures des livres dans un dossier "imgs". Dans un autre dossier "csvfile", il récupèrera les informations de chaque livre dans des fichiers CSV au nom de chaque catégorie.


**Enjoy!! :)**
	



