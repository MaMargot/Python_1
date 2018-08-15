# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import urllib
def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return(html)
def getimg(html):
  reg=r'src="(.+?\.jpg)"pic_ext'
  imgre=re.compile(reg)
  imglist=re.findall(imgre,html)
  x=0
  for imgurl in imglist:
      urllib.urlretieve(imgurl,'D:\个人相片\python\\s.jpg')
      x+=1
  return imglist
html=gethtml("http://tieba.com/p/2460150866")      
print getimg(html)
      
  