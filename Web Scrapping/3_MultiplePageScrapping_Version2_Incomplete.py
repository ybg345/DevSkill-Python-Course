from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

scrap_url = 'http://quotes.toscrape.com'
urlClnt = urlopen(scrap_url)
raw_html = urlClnt.read()
urlClnt.close

page = soup(raw_html, 'html.parser')
containers = page.findAll('div', {'class' : 'quote'})
container = containers[0]

with open('test.csv', 'w') as f:
    f.write('Quote,Author,Tags\n')
    
    for container in containers:
        Quote = container.find('span', {'class' : 'text'}).text.replace('“',r'').replace(',','').replace('”','')
        Author = container.find('small',{'class' : 'author'}).text
        Tags = container.find('meta', {'class': 'keywords'})['content'].replace('-',' ').replace(',','-')
        
        f.write(Quote + ',' + Author + ',' + Tags + '\n')

navigator = page.findAll('div', {'class' : 'col-md-8'})
navigat = navigator[1]
u = navigat.nav.a['href']
# len(u)
url = scrap_url + u
url
scrap_url = url
scrap_url    # getting next page url while existing in current page. 


# What i want to do now:

# I have got a new url in the 'scrap_url' variable in the last line. Now, I want to send the new 'scrap_url' 
# to the beginning 'scrap_url' and update the beginning 'scrap_url' with new value and 
# continue the whole process as long as we get different value for 'scrap_url'(at the end) and 'scrap_url'(at the beginning)

# If we can loop over this process then we will use 'append' mode in file instead of 'write mode'