# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 21:23:22 2018

@author: jerry.liu
"""
from bs4 import BeautifulSoup
import requests
import re
import json
html = requests.get('http://citeseerx.ist.psu.edu/search?q=recurrent+neural+network&submit.x=0&submit.y=0&submit=Search&sort=rlv&t=doc').content
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
Tags=soup.find_all('div',class_='result')    
for changepage in range(1,0,-1):
 for tag in Tags:
    Url=tag.a['href']
    TAYdata=tag.getText().split('...',1)
    TAYdata[0]=TAYdata[0].strip()
    TAYdata[0]=re.sub('\s+', ' ', TAYdata[0])
    print '\n\n\n'+'Url=  http://citeseerx.ist.psu.edu'+Url+'\n\n\n'
    TAYsort1=TAYdata[0].split('by',1)
    Title=TAYsort1[0]
    year=re.findall(r'[0-9]+',TAYsort1[1])
    stry=''.join(year)
    if stry.isdigit():
     authors=TAYsort1[1].split(', '+stry)
    print Title+'\n'
    print stry+'\n'
    print authors[0]
    html = requests.get('http://citeseerx.ist.psu.edu'+Url).content
    Soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')#carefully about the "Soup"#
    Abstract=Soup.find('div',{"id":"abstract"}).getText()
    Result='{"Title":'+'"'+TAYsort1[0]+'",'+'"Authors":"'+authors[0]+'",'+'"Year":"'+stry+'",'+'"Abstract":"'+Abstract+'"}\n'
    print Abstract
    print Result
    with open ('CiteSeerX.json','a')as f:
     json.dump(Result,f,sort_keys = True ,indent = 4) 
 nextpage='http://citeseerx.ist.psu.edu'+soup.find('div',{"id":"pager"}).a['href']
 print nextpage