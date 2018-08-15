# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 12:27:42 2016

@author: MaMargot
"""

    #coding:utf-8  
import urllib2  
import time  
from bs4 import BeautifulSoup  
time.clock()
class YZBZ():  
    def __init__(self):  
        self.pageIndex = 1  
        self.user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        self.headers = { 'User-Agent' : self.user_agent }  
    def getHtml(self,pageIndex):  
        try:  
            url='http://db.yaozh.com/biaozhun?p='+ str(pageIndex)  
            request=urllib2.Request(url,headers=self.headers)  
            page=urllib2.urlopen(request)  
            html=page.read()  
            return html  
        except urllib2.URLError,e:  
            if hasattr(e,"reason"):  
                print u"连接失败",e.reason  
                return None  
    def getItems(self):  
        L=range(1,11)  
        for pageIndex in L:  
            html=self.getHtml(pageIndex)  
            soup=BeautifulSoup(html)  
            tr_list=soup.find_all("tr")  
            #写入表格标题  
            if pageIndex==1:  
                with open(r"C:\Users\MaMargot\Desktop\aaa.txt","a+") as a:  
                    a.write((tr_list[0].get_text("|",strip=True).encode("utf-8")+"|"+"\n"))  
            #写入表格内容  
            f=open(r"C:\Users\MaMargot\Desktop\aaa.txt","a+")  
            #主要是数据中有空白项，若不将空白进行替换数据项将无法对齐  
            for tr in tr_list[1:]:  
                f.write('\n')  
                for item in tr:  
                    if item not in ('',' ','\n'):  
                          if item.string==None:  
                              f.write("None"+"|")  
                          else:  
                              f.write(item.string.encode('utf-8')+'|')  
            f.close()  
      
      
spider=YZBZ()  
spider.getItems() 
print(time.clock())