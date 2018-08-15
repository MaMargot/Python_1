# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 10:57:30 2016

@author: MaMargot
"""

import urllib2
response = urllib2.urlopen('http://192.168.1.102:8181/static/index.html')
html = response.read()
print html