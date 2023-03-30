#web scrapping
# Using the following website https://www.scrapethissite.com/pages/simple/ I was able to extract all the different countries with their respective variables.

import requests
from bs4 import BeautifulSoup
from csv import writer

URL = "https://www.scrapethissite.com/pages/simple/"
r = requests.get(URL)
print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

soup1 = BeautifulSoup(r.content, 'html.parser')
lists = soup.find_all('div',class_="col-md-4 country")
lists

with open('countries.csv','w', encoding='utf8',newline="") as f:
    thewriter=writer(f)
    header=['country_name','capital','population','Area_km2']
    thewriter.writerow(header)
    for list in lists:
        country_name = list.find('h3', class_="country-name").text.replace('\n', '')
        capital= list.find('span', class_="country-capital").text.replace('\n', '')
        population=list.find('span',class_="country-population").text.replace('\n', '')
        Area_km2=list.find('span',class_="country-area").text.replace('\n', '')
        info=[country_name,capital,population,Area_km2]
        thewriter.writerow(info)
        
       
