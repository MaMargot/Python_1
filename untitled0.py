# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 13:58:10 2016

@author: MaMargot
"""
##读取网站源代码
import urllib2
response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()
print html



##请求与发送
import urllib2
req = urllib2.Request('ftp://baidu.com')
response= urllib2.urlopen(req)
the_page = response.read()
print the_page



##发送data表单数据（post）
import urllib2,urllib
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
name=Somebody+Here&language=Python&location=Northampton#删去
url='http://www.example.com/example.cgi'
full_url=url+'?'+url_values
data=urllib2.open(full_url)




##设置Header到HTTP请求，不可用，但原理可借鉴
import urllib,urllib2
url='http://www.somesever.com/cegi-bin/register,cgi'
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
values={'name':'WHY','location':'SDU','language':'Python'}
headers={'user-Agent':user_agent}
data=urllib.urlencode(values)
req=urllib2.Request(url,data,headers)
respnse=urllib2.uropen(req)
the_page = resopnse.read()



##URLError
import urllib2
req=urllib2.Request('http://www.baibai.com')
try:urllib2.urlopen(req)
except urllib2.URLError,e:
    print e.reason
    

