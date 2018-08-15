# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:42:48 2016

@author: MaMargot
"""
import urllib2
import urllib
import BeautifulSoup
import time
time.clock()
##########第一步，网站的获取方法
##读取网站源代码
response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()
print html

def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return(html)
##请求与发送（通常方式）
req = urllib2.Request('ftp://baidu.com')
response= urllib2.urlopen(req)
the_page = response.read()
print the_page
##发送data表单数据（post）
url='http://www.someserver.com/register.cgi'
values={'name':'why','loaction':'SDU','language':'python'}
data=urllib.urlencode(values)#编码工作
req=urllib2.Request(url,data)#发送请求同时传data表单
response=urllib2.urlopen(req)#接受反馈的信息
the_page=response.read()#读取反馈的内容
##发送data表单数据（GET）
import urllib2,urllib
data={}
data=['name']='WHY'
data=['location']='SDU'
data=['language']='Python'
url_values=urllib.urlencode(data)
print url_values
url='http://www.example.com/example.cgi'
full_url=url+'?'+url_values
data=urllib2.open(full_url)
##设置Header到HTTP请求，不可用，但原理可借鉴（重要，模拟浏览器）
import urllib,urllib2
url='http://www.somesever.com/cegi-bin/register,cgi'
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
values={'name':'WHY','location':'SDU','language':'Python'}##不一定需要
headers={'user-Agent':user_agent}
data=urllib.urlencode(values)
req=urllib2.Request(url,data,headers)
respnse=urllib2.uropen(req)
the_page = resopnse.read()