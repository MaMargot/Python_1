# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:55:07 2016

@author: MaMargot
"""
##列表
edward=['Edward Gumby',42]
edward
john=['Jhon Smith',50]
database=[edward,john]
greeting="Hello"
greeting[0]###python从0开始
greeting[-1]
'Hello'[-1]
fourth=raw_input("Year:")[3]
fourth=raw_input("Year:")
next=input("Year:")
2015
fourth
##索引示例
months=['January','February','March','April','May','June','July','August','September','October','November','December']
months[0]
##以1~31的数字作为结尾的列表
endings=['st','nd','rd']+17*['th']\
+['st','nd','rd']+7*['th']\
+['st']
endings
year=raw_input('Year:')
1974
month=raw_input('Month(1-12):')
8
day=raw_input('Day(1-31):')
16
month_number=int(month)
day_number=int(day)
##记得要将月份和天数减1，以获得正确的索引
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]
print month_name+' '+ordinal+"."+year
tag='<a href="http://www.python.org">python web site</a>'
tag[9:30]
tag[32:-4]
numbers=[1,2,3,4,5,6,7,8,9,10]
numbers[3:6]####无法实现不连续值的同时索引
numbers[0:1]
numbers[-1:-3]
numbers[-3:-1]
numbers[-3:0]
numbers[-3:]
numbers[:3]
numbers[:]
url=raw_input("Please enter the URL:")
http://www.something.com
domain=url[11:-4]
print "Domain name:"+domain
numbers[0:10:1]#设置步长
numbers[0:10:2]
numbers[0:10:3]
numbers[::4]
numbers[8:3:-1]
numbers[10:0:-2]
numbers[-3:0:-1]##理解
numbers[0:10:-2]##理解
numbers[::-2]
numbers[5::-2]#理解
numbers[:5:-2]
[1,2,3]+[4,5,6]##序列相加
"Hello."+"world!"
[1,2,3]+"world!"##列表与字符串不能相加
["Hello"]+"world!"
["Hello."]+["word!"]##注意区别
'python'*5
[14]*5
sequence=[None]*10
sequence
##乘法
sentence=raw_input("sentence:")
"He's a very naughty boy!"
screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width-text_width)//2
middle_margin=(box_width-text_width)//2
print
print ' '*left_margin+'+'+'-'*(box_width-2)+'+'
print ' '*left_margin+'|'+' '*(box_width-2)+'|'
print ' '*left_margin+'|'+' '*(middle_margin-1)+sentence+' '*(middle_margin-1)+'|'
print ' '*left_margin+'|'+' '*(box_width-2)+'|'
print ' '*left_margin+'+'+'-'*(box_width-2)+'+'
##成员资格
permission='rw'
'w' in permission
'x' in permission
users=['mlh','foo','bar']
raw_input('Enter your user  name:') in users
mlh
subject='$$$ GET rich now !!! $$$'
'$$$' in subject
'p' in 'python'
'p' in 'ppython'
'pp' in 'python'
database=[['albert','1234'],['dilbert','4242'],['smith','7524'],['jones','9843']]
usersname=raw_input('User name:')
pin=raw_input('PIN code:')
if[usersname,pin] in database : print 'Access granted'
numbers=[100,34,678]
print len(numbers)
print max(numbers)
print min(numbers)
print max(2,3)
print min(9,3,2,5)
list('Hello!')
list('1234')
' '.join('Hello')
x=[1,1,1]
x[1]=2 ##给列表中的元素赋新值
x
names=['Alice','Beth','Cecil','Dee=Dee','Earl']
del names[2] ##删除列表中的元素
name=list('Perl')
name
name[2:]=list('ar')###分片的强大之处如下：
name
name=list('Perl')
name[1:]=list('ython')###替换更长的元素
name
numbers=[1,5]
numbers[1:1]=[2,3,4]###插入新元素
numbers
numbers[1:4]=[]###删除元素
numbers
lst=[1,2,3]
lst.append(4)##方法：序列追加1个元素
lst
a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)##方法：序列追加多个元素
a
['to','be','or','not','to','be'].count('to')
x=[[1,2],1,1,[2,1,[1,2]]]
x.count(1)##方法：序列计数
x.count([1,2])
a=[1,2,3]###序列连接
b=[4,5,6]
a+b
a
a=a+b
a=[1,2,3]
b=[4,5,6]
a[2:]=b###分片插入新元素（a[len(2):]=b）
a
import numpy as np ##序列之间进行算数运算
a=np.array(a)
b=np.array(b)
s=a+b
knights=['We','are','the','knights','who','say','ni']###寻找某个值第一次出现的索引值
knights.index('who')
knights.index('herring')
numbers=[1,2,3,4,5,6,7]###列表中插入某元素,参数1为那个元素前插入
numbers.insert(3,'four')
numbers
numbers=[1,2,3,4,5,6,7]###同上
numbers[3:3]=['four']
numbers
x=[1,2,3]###列表中删去某一元素
x.pop()
x
x.pop(0)
x
x=[1,2,3]###模拟数据结构：栈，先进后出
x.append(x.pop())
x
x=['to','be','or','not','to','be']###列表中移除某个值
x.remove('be')##只移除了第一次出现的值
x.remove('bee')
x=[1,2,3,4]###列表中元素反向存放
x.reverse()
x
x=[1,2,3]
reversed(x)###反向存放，但返回的是迭代器，非list
list(reversed(x))
x=[4,6,2,1,7,9]###对列表原位置进行排序
x.sort()
x
x=[4,6,2,1,7,9]
y=x.sort()###DON'T do this
x
y
print y
y=x[:]###使用分片的方式赋值，创建了新列表
y.sort()
x
y
y=x###x，y同时指向同一个列表，x，y均改变
y.sort()
x
y
x=[4,6,2,1,7,9]###使用sorted函数，创建了已排序的副本
y=sorted(x)
x
y
sorted('python')###可用于任何序列，返回一个列表
sorted.reverse()###不懂
cmp(42,32)
cmp(99,100)
cmp(10,10)
numbers=[5,2,7,9]
numbers.sort(cmp)###使用compare（x，y）函数来定义排序顺序，####有点不懂
numbers
x=['aardvark','abalone','acme','add','aerate']
x.sort(key=len)##关键词key，定义根据元素长度来进行排序
x
x=[4,6,2,1,7,9]
x.sort(reverse=True)
x
1,2,3###创建元组
(1,2,3)
()
42##无法创建元组
(42)##无法创建元组
42,###加上，即可创建单值元组
(42,)
3*(40+2)##非元组
3*(40+2,)###元组
tuple([1,2,3])###tuple函数用于将列表转化为元组
tuple('abc')
tuple((1,2,3))
x=1,2,3###元组的操作
x
x[1]
x[0:2]
x[2]
x=[1,2,3]
x[0:2]
website='http://www.python.org'
website[-3:]='com' #ERROR
formats="Hello,%s.%s enough for ya?"#格式化字符串
values=('world','Hot')
print formats%values
format = "pi with three decimals : %.3f" #保留小数点后几位的浮点数
from math import pi
print format%pi
from string import Template##模板字符串
s=Template('$x.glorious $x!')
s.substitute(x='slurm')
s=Template("It's ${x}tastic!")#插入单词的一部分
s.substitute(x="slurm")
s=Template('Make $$ selling $x!')#插入美元符号
s.substitute(x='slurm')
s=Template('A $thing must never $action.')#使用字典变量提供值/名称对
d={}
d['thing']='gentleman'
d['action']='show his sock'
d
s.substitute(d)
'%s plus %s equals %s'%(1,2,3)
help(str)
help(repr)
'price of eggs : $%d'%42 ###转化为十进制整数
'Hexadecimal price of eggs:%x'%42###转化为十六进制
from math import pi###十进制浮点数
'pi:%f...'%pi
'Very inexact estimate of pi :%i'%pi###转化为十进制实数
'Using str:%s'%42L###转化为字符串
'Using repr:%r'%42L###转化为字符串，不改变形式
'%10f'%pi###字段宽10
'%10.2f'%pi###字段宽10，精度2
'%.2f'%pi###精度为2
'%.5s'%'Guido van Rossum'###包含最大字符个数为5
'%.*s'%(5,'Guido ban Rossum')###使用*符号作为字段宽度或精度
'%010.2f'%pi###0填充
010###以0开头8进制
'%-10.2f'%pi###左对齐
print('% 5d'%10)+'\n'+('% 5d'%-10)###整数加空格，起对齐正负数的作用
print('%+5d'%10)+'\n'+('%+5d'%-10)###整数加符号，起区分正负数的作用
#使用给定的宽度打印格式化后的价格列表
width=input('Please enter width:')
price_width=10
item_width=width-price_width
header_format='%-*s%*s'
format='%-*s%*s'
print '='*width
print header_format%(item_width,'Item',price_width,'Price')
print '-'*width
print format % (item_width,'Apple',price_width,0.4)
print format % (item_width,'Pears',price_width,0.5)
print format % (item_width,'Cabtaloupes',price_width,1.92)
print format % (item_width,'Dried Apricots(16 oz)',price_width,8)
print format % (item_width,'Pruens (4 1bs)',price_width,12)
print '='*width
####例子
'With a moo-moo here.and a moo-moo there'.find('moo')###find函数
title="Monty Python's Flying Circus"
title.find('Monty')###返回子串所在位置的最左端索引
title.find('Python')
title.find('Flying')
title.find('Zirquss')###没有找到返回-1
subject='$$$ Get rich now !!! $$$'
subject.find('$$$')
subject.find('$$$',1)###指定起始位置
subject.find('!!!')
subject.find('!!!',0,16)###指定起始位置，同时指定终止位置，但要注意python的规则
seq=[1,2,3,4,5]####添加元素，要求序列元素是字符或字符串
sep='+'
sep.join(seq)
seq=['1','2','3','4','5']
sep.join(seq)
dirs='','usr','bin','env'
'/'.join(dirs)
print 'C:'+'\\'.join(dirs)###根据系统约定使用不同的间隔符
'Trondheim Hammer Dance'.lower()###转化为小写
if 'Gumby' in ['gumby','smith','jones']: print 'Found it'
name='Gumby'
names=['gumby','smith','jones']
if name.lower() in names : print 'Found it' 
"that's all folks".title()###使用title（）函数使首写字母大些
import string
string.capwords("that's all folks")###使用capword使首写字母大写
'This is a test'.replace('is','ezz')###字符串的替换
'1+2+3+4+5'.split('+')###join的逆方法，将字符串分割成序列
'/usr/bin/env'.split('/')
'Using the default'.split()###不提供分隔符下，将所有空格，制表，换行等当作分隔符
'     interal whitespace is kept        '.strip()###除去两侧不包括内部的分隔符
###对比lower的方法
names=['gumby','smith','jones']
name='gumby '
if name in names:print 'Found it'
if name.strip() in names : print 'Found it'
'****SOAM * for * everyone!!! ***'.strip(' *!')###除去指定的字符


from string import maketrans ###maketrans(fm,to)两个等长的字符串，表示第一个字符串中的每个字符都用第二个字符串中相同位置的字符替换。
table=maketrans('cs','kz')###转换表是包含替换ASCII字符集的替换字母的字符串
len(table)
table[97:123]
maketrans(" "," ")[97:123]
'this is an incredible test'.translate(table)
'this is an incredible test'.translate(table,' ')###可选参数，‘ ’删除指定需要删除的字符
print 'BΦLLEFRΦ'.lower()
table=maketrans('Φ','θ')###希腊字母可通过translate转换得到
word='KAPESΦM'
print word.lower()
print word.translate(table)
print word.translate(table).lower()

names=['Alice','Beth','Cecil','Dee-Dee','Earl']
numbers=['2341','9102','3158','0142','5551']
numbers[names.index('Cecil')]
phonebook={'Alice':'2341','Beth':'9102','Cecil':'3158'}###字典,键是唯一的，但值不是唯一的
items=[('names','Gumby'),('age',42)]
d=dict(items)###建立字典
d
d=dict(names='Gumby',age=42)
d
###len(d)返回键-项的数量；d[k]返回键上的值；d[k]=v将值v赋值到键k上
###del[k]删除键为k的项；k in d 检查d中是否有键为k的项
###在字典中检查键的成员资格比在列表中检查值的成员资格更高效，数据结构的规模越大，两者的效率差距越明显
###键可以为任何不可变类型
x=[]
x[42]='Foobar'
x={}
x[42]='Foobar'
x
people={'Alice':{'phone':'2341','addr':'Foo drive 23'},'Beth':{'phone':'9102','addr':'Bar street 42'},'Cecil':{'phone':'3158','addr':'Baz avenue 90'}}
labels={'phone':'phone number','addr':'address'}
name=raw_input('Name :')
request=raw_input('Phone or Adress:')
if request == 'p' : key='phone'
if request =='a' : key='addr'
if name in people : print " %s's %s is %s."%\
(name,labels[key],people[name][key])
phonebook={'Beth':'9102','Alice':'2341','Cecil':'3258'}
"Cecil's phone number is %(Cecil)s."% phonebook
template='''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data={'title':'My Home Page','text':'Welcome to my home page!'}
print template % data
d={}
d['name']='Gumby'
d['age']=42
d
return_value=d.clear()
d
print return_value
x={}
y=x
x['key']='value'
y###注意前面的索引指向问题,x和y最初对应同一个字典
x={}###通过将关联到一个新的空字典，无法对y清空
y
x{}
x.clear()###清空原始字典中的所有元素
y
x={'username':'admin','machines':['foo','bar','baz']}
y=x.copy()###返回一个具有相同键-值对的新字典(浅复制),在副本中替换值时，原始字典不受影响，但是，如果修改某个值，原始字典也会改变
y['username']='mlh'
y['machines'].remove('bar')
y
x
from copy import deepcopy###深复制
d={}
d['names']=['Alfred','Bertrand']
c=d.copy()
dc=deepcopy(d)
d['names'].append('Clive')
c
dc
{}.fromkeys(['name','age'])
dict.fromkeys(['name','age'])
dict.fromkeys(['name','age'],'(unknown)')
d={}
print d['name']
print d.get('name')
d.get('name','N/A')
d['name']='Eric'
d.get('name')
labels={'Phone':'Phone number','Addr':'Address'}
name=raw_input("Name:")
request=raw_input("Phone number (p) or Address (a) :")
key=request
if request=='p' : key='Phone'
if request =='a' :key ='Addr'
person=people.get(name,{})
label =labels.get(key,key)
result=person.get(key,'not available')
print "%s's %s is %s."%(name,label,result)
d={}
d.has_key('name')
d['name']='Eric'
d.has_key('name')
d={'title':'python web site','url':'http://www.python.org','spam':0}
d.items()###同样keys返回键的列表
d
it=d.iteritems()
it
list(it)###多数情况下，iteritems更高效，同样iterkeys返回键的迭代器
d={'x':1,'y':2}
d.pop('x')
d
d.popitem()###弹出随机项，若想一个接一个地移除并处理项，该方法非常有效
d
d={}
d.setdefault('name','N/A')###类似于get，能够获得与给定的键相关联的值，还能在字典中不含有给定键的情况下设定相应的键值
d
d['name']='Gumby'
d.setdefault('name','N/A')
d
d={}
print d.setdefault('name')
d
d={'titile':'Python Web Site','url':'http://www.python.org','changed':'Mar 14 22:09:15 MET 2018'}
x={'title':'Python Language Website'}
d.update(x)###可以使用或调用dict函数（或类型构造函数）同样的方式进行调用
d
d={}
d[1]=1
d[2]=2
d[3]=3
d[4]=1
d.values()###以列表形式返还字典中的值，itervalues返回值的迭代器














