from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.nytimes.com/2022/01/08/us/teachers-unions-covid-schools.html').text

soup = BeautifulSoup(source, 'lxml')

print('----------')
print(f'TITLE: {soup.title.string}')
print('----------')
print(f'H1: {soup.h1.string}')
print(f'H2: {soup.h2.string}')
print(f'H3: {soup.h3.string}')
print('----------')
article_summary = soup.find('p', class_='css-w6ymp8 e1wiw3jv0').text
print(f'Article summary: {article_summary}')
print('----------')
image_summary = soup.find('span', class_='css-16f3y1r e13ogyst0').text
print(f'Image summary: {image_summary}')
print('----------')
authors = soup.find('p', class_= 'css-aknsld e1jsehar1')
author1 = authors.find('span', class_= 'css-1baulvz').text
author2 = authors.find('span', class_= 'css-1baulvz last-byline').text
print(f'Authors: {author1} and {author2}')
print('----------')

# for item in soup.select('.StoryBodyCompanionColumn'):
#     try:
#         para = item.find_all('p')
#         print(para)
#     except Exception as e:
#         print('f')


for item in soup.select('.StoryBodyCompanionColumn p'):
    try:
        para = item.text
        print(para)
    except Exception as e:
        print('f')
