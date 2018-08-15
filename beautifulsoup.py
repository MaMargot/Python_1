# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 10:12:27 2016

@author: MaMargot
"""

from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html)
print soup.prettify()#格式化输出
print soup.title
print soup.head
print soup.a
print soup.p
print type(soup.a)
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p['class']
print soup.p.get('class')
soup.p['class']="newclass"
del soup.p['class']
print soup.p
print soup.p.string
print type(soup.p.string)
print type(soup.name)
print soup.name
print soup.attrs
##带注释的标签
print soup.a
print soup.a.string
print type(soup.a.string)
if type(soup.a.string)=='bs4.element.Comment':
    print soup.a.string
print soup.head.contents
print soup.head.contents[0]
print soup.head.children
for child in  soup.body.children:
    print child
for child in soup.descendants:
    print child    
print soup.head.string
print soup.title.string    
print soup.html.string    
for string in soup.strings:
    print(repr(string)) 
for string in soup.stripped_strings:
    print(repr(string))
p = soup.p
print p.parent.name
content = soup.head.title.string
print content.parent.name	
content = soup.head.title.string
for parent in  content.parents:
    print parent.name