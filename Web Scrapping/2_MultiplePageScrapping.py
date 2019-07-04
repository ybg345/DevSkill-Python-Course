                                                    # Author: Mehedi Afzal Farazi
#Problem:
#                               Scrape all data from this url "http://quotes.toscrape.com/" from all the pages
#                               And dump the scrape data in a csv file.
#                               Column Header will be Quote, Author, Tags.
#                               All the tags will be in one cell and they will be separated by hifen "-"

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


for num in range(1,11):    
    scrap_url = 'http://quotes.toscrape.com/page/{}'.format(num)
    urlClnt = urlopen(scrap_url)
    raw_html = urlClnt.read()
    urlClnt.close

    page = soup(raw_html, 'html.parser')
    containers = page.findAll('div', {'class' : 'quote'})
    container = containers[0]

    with open('scrapping.csv', 'a', encoding="utf8") as f:          
        f.write('Quote,Author,Tags\n')

        for container in containers:
            Quote = container.find('span', {'class' : 'text'}).text.replace('“',r'').replace(',','').replace('”','')
            Author = container.find('small',{'class' : 'author'}).text
            Tags = container.find('meta', {'class': 'keywords'})['content'].replace('-',' ').replace(',','-')

            f.write(Quote + ',' + Author + ',' + Tags + '\n')



# Some comments:
#   * At line 12 and 13 we are generating url for every page and loop through every page. 

#   * At line 22 we have to give (encoding="utf8") because if we do not give it, 
#     for webpage 8 we will get (UnicodeDecodeError: 'charmap' codec can't decode) 

#   * We are using file mode 'append' in line 22 for writing the data. We we give 'write' mode
#     then it will scrap all the pages and finally stores page 10 data after final overwrite in the file. 