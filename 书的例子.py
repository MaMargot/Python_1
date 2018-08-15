# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:13:54 2016

@author: MaMargot
"""

print "Hello,World!"
2+2
25353672+235
1/2
1.0/2
1/2.
1//2 #整除
1.0//2.0
10%3##求余
10/3
2**3#取幂运算
x=3
x*2
x=input("x:")
x
pow(2,3)#取幂
round(4.25)
import math
math.floor(32.9)
int(math.floor(32.9))###int会自动向下取整
from math import sqrt###from 模块 import 函数，但会造成命名的冲突
sqrt(9)###则不需要加前缀
import cmath ###负数运算
cmath.sqrt(-1)
name=raw_input("What is your name:")
print "Hello"+name+"!"
"Hello,world!"
"Let's go!"
'Let's go!'  #错误例子
'"Hello world!"she said'
"\"Hello world!\"she said"
"Let's say"'"Hello,world!"'
x="Hello."
y="world!"
x y   #错误例子,只有在同时写下两个字符串是才可以自动拼接他们
x+y
10000L
print x+y ###只有在print下才可以实现转义等的功能
print 1000L
print repr("Hello world!")###创建一个字符串
print repr(10000L)
print str("Hello world!")###把值转化为合理形式的字符串
print str(10000L)
temp=42
print "the temperature is"+ temp
print "the temperature is"+ `temp`###反引号的功能类似repr()函数 
name=input("What is your name?")###需要输入合法的python表达式
"mcj"
print "Hello "+name+" !"
input("Enter a number:")
3
raw_input("Enter a number")###会将所有输入当作原始数据，并放入字符串中
3
print '''This is a very long string.  #长字符串
It continues here.
And It's not over yet.
"Hello.world!"
still here'''
print "Hello.\
  world!"#普通字符串
print 1+2\
+3+4
print \
  'Hello.world!'
print 'Hello.\n world!'
path='c:\nowhere'
path
print path
path='c:\\nowhere'
print r'C:\nowhere'#原始字符串
print r'This is illegal\'
print r'C:\\program Files\foo\bar''\\'#以\结束的解决办法之一
u'Hello world!'
print r'Let\'s go!'
