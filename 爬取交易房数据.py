# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 12:25:18 2016

@author: MaMargot
"""

import urllib2  
import time    
from bs4 import BeautifulSoup  
time.clock()  
for i in range(101):  
    url = 'http://sz.lianjia.com/ershoufang/pg'+str(i)+'/'  
    page = urllib2.urlopen(url)  
    soup = BeautifulSoup(page)  
    for link in soup.find_all('div','houseInfo'):  
         context = link.get_text()  
         print(context)  
print(time.clock())  