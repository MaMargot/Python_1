# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 16:37:01 2016

@author: MaMargot
"""
import re
import urllib2
import MYSQLdb
from Beatifulsoup import BeautifulSoup

url1="http://bbs.ustc.edu.cn/cgi/bbstdoc?board=PieBridge&start=3558"
fp=urllib2.urlopen(url1)
s=fp.read()
soup=BeautifulSoup(s)
polist=soup.findALL('span')
print polist[0].content[0]
