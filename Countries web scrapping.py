#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from csv import writer


# In[2]:


URL = "https://www.scrapethissite.com/pages/simple/"
r = requests.get(URL)
print(r.content)


# In[3]:


soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())


# In[4]:


soup1 = BeautifulSoup(r.content, 'html.parser')


# In[5]:


lists = soup.find_all('div',class_="col-md-4 country")


# In[6]:


lists


# In[12]:


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


# In[ ]:




