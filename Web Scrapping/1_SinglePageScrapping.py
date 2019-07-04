                                                    # Author: Mehedi Afzal Farazi
#Problem:
#                               Scrape all data from this url "http://quotes.toscrape.com/" i.e. Home page
#                               And dump the scrape data in a csv file.
#                               Column Header will be Quote, Author, Tags.
#                               All the tags will be in one cell and they will be separated by hifen "-"

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

scrap_url = 'http://quotes.toscrape.com/'
urlClnt = urlopen(scrap_url)
raw_html = urlClnt.read()
urlClnt.close

page = soup(raw_html, 'html.parser')
containers = page.findAll('div', {'class' : 'quote'})
container = containers[0]

with open('scrapping.csv', 'w') as f:
    f.write('Quote,Author,Tags\n')
    
    for container in containers:
        Quote = container.find('span', {'class' : 'text'}).text.replace('“',r'').replace(',','').replace('”','')
        Author = container.find('small',{'class' : 'author'}).text
        Tags = container.find('meta', {'class': 'keywords'})['content'].replace('-',' ').replace(',','-')
        
        f.write(Quote + ',' + Author + ',' + Tags + '\n')

