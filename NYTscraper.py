from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(filename='scraper.log', level=logging.DEBUG)

url = input("Enter the url: ")
source = requests.get('https://www.' + url).text
soup = BeautifulSoup(source, 'lxml')
nyt = "nytimes.com"

if nyt in url:
    logging.debug('----------------------------------------')
    logging.debug('----------------------------------------')
    logging.debug(f'TITLE: {soup.title.string}')
    logging.debug('----------------------------------------')
    logging.debug(f'H1: {soup.h1.string}')
    logging.debug(f'H2: {soup.h2.string}')
    logging.debug(f'H3: {soup.h3.string}')
    logging.debug('----------------------------------------')
    article_summary = soup.find('p', class_='css-w6ymp8 e1wiw3jv0').text
    logging.debug(f'Article summary: {article_summary}')
    logging.debug('----------------------------------------')
    image_summary = soup.find('span', class_='css-16f3y1r e13ogyst0').text
    logging.debug(f'Image summary: {image_summary}')
    logging.debug('----------------------------------------')
    authors = soup.find('p', class_= 'css-aknsld e1jsehar1')
    author1 = authors.find('span', class_= 'css-1baulvz').text
    author2 = authors.find('span', class_= 'css-1baulvz last-byline').text
    logging.debug(f'Authors: {author1} and {author2}')
    logging.debug('----------------------------------------')
    logging.debug('----------------------------------------')

    for item in soup.select('.StoryBodyCompanionColumn p'):
        try:
            para = item.text
            logging.debug(para)
        except Exception as e:
            logging.debug('f')

    logging.debug('----------------------------------------')
    logging.debug('----------------------------------------')
    logging.debug('----------------------------------------')
    logging.debug('----------------------------------------')
    logging.debug('----------------------------------------')

else:
    print("Error! Is this site supported yet? If it should be and still gave this error, double check your url.")
    logging.debug("Error! Is this site supported yet? If it should be and still gave this error, double check your url.")