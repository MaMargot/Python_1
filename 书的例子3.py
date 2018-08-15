# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 01:01:50 2018

@author: MaMargot
"""

print 'Age:',42
1,2,3
print 1,2,3
print (1,2,3)
name='Gumby'
salutation='Mr'
greeting='Hello.'
print greeting,salutation,name
print greeting,',',salutation,name
print greeting+',',salutation,name###不加空格
print 'Hello',###在结尾处加上逗号，那么接下来的语句会与前一条语句在同一行打印
print 'World.'
import somemodule###从模块导入函数
from somemodule import somefunction
from somemodule import somefunction,anotherfunction,yetanotherfunction
from somemodule import *
module1.open(...)###如果两个模块中同时含有相同函数的调用方法
module2.open(...)
import math as foobar ###或者在语句末尾加上as子句，并给出子句的名字，或为模块提供别名
foobar.sqrt(4)
from math import sqrt as foobar ###为函数提供别名
foobar(4)
###序列解包(对元组)-将多个值的序列解开，然后放到变量的序列中
x,y,z=1,2,3###多个赋值操作同时进行
print x,y,z
x,y=y,x###交换两个(或更多)变量,跳过了中间变量
print x,y,z
values=1,2,3
values
x,y,z=values
x
###使用popitem方法，获取字典中的任意键-值对，作为元组返回
scoundrel={'name':'Robin','girlfriend':'Marion'}
key,value=scoundrel.popitem()
key
value
x,y,z=1,2###所解包的序列中的元素数量必须和放置在赋值符号=左边的变量数量完全一致
x,y,z=1,2,3,4
###链式赋值将同一个值赋给多个变量的捷径
x=y=somefunction()###只处理一个值
y=somefunciion()
x=y###与上等效
x=somefunction()
y=somefunction()
###增值赋值
x=2
x+=1
x*=2
x
fnord='foo'
fnord+='bar'
fnord*=2
fnord

###条件
True
False
True==1
False==0
True+False+42
bool('I think,therebefore i am')
bool(42)
bool(0)
name=raw_input('What is your name?')
if name.endswith('Gumby'):
    print 'Hello,Mr.Gumby'
if name.endswith('Gumby'):
    print 'Hello,Mr.Gumby'
else:
    print 'Hello,stranger'
num=input('Enter a number: ')
if num>0 :
    print 'The number is positive'
elif num<0 :
    print 'The number is negative'
else:
    print 'The number is Zero'
name=raw_input('What is your name?')
if name.endswith('Gumby'):
    if name.startswith('Mr'):
        print 'Hello,Mr.Gumby'
    elif name.startswith('Mrs'):
        print 'Hello,Mrs Gumby'
else:
    print 'Hello,stranger'
###x is  y :x和y是同个对象，x is not y ：x和y不是同个对象
###is同一性运算符
x=y=[1,2,3]
z=[1,2,3]
x==y
x==z
x is y
x is z ###  !!!
x=[1,2,3]
y=[2,4]
x is not y
del x[2]
y[1]=1
y.reverse()
x==y
x is y
name=raw_input('What is your name?')
if 's' in name :
    print 'Your name contains the letter "s".'
else:
    print 'Your name does not contains the letter "s". '
"alpha"<"beta"
'FnOrD'.lower()=='Fnord'.lower()
[1,2]<[2,1]
[2,[1,4]]<[2,[1,5]]
number=input('Enter a number between 1 and 10:')
if number<=10 and number >=1:
    print 'Great!'
else: 
    print 'Wrong!'
#if((cash>price) or customer_has_good_credit) and not out_of_stock: give_goods()
#assert断言（作为初期调试或调试过程中的辅助条件）
age=10
assert 0<age<100
age=-1
assert 0<age<100
###如果需要确保程序中的某一条件一定为真时才能让程序正常工作的话，assert语句可以在程序中插入检查点
age=-1 
assert 0<age<100,'The age must be realistic' ###条件后添加字符串，用于解释断言

###循环
x=1
while x<=100:
    print x
    x+=1
name=''
while not name:### not name or not name.isspace()   /while not name.strip()
    name=raw_input('Please enter your name:')
print 'Hello,%s!'%name
words=['this','is','an','ex','parrot']
for word in words:
    print word
numbers=[0,1,2,3,4,5,6,7,8,9]
for number in numbers:
    print number
range(0,10)
range(10)###它包含下限，但不包含上限，可以只提供上限
for number in range(1,101):
    print number
###xrange()与range()作用类似，区别在于rang函数一次创建整个序列，而xrange()一次只创建一个数。
d={'x':1,'y':2,'z':3}
for key in d :
    print key ,'corresponds to',d[key]
##x=d.iterkeys()获取字典中的键的迭代器 /d.key() 获取键
##list(x)获取迭代器中的键
for key,value in d.items(): ###d.items、d.keys、d.values 
    print key,'corresponds to',value

###并行迭代
names=['anne','beth','george','damon']
ages=[12,45,32,102]
for i in range(len(names)):
    print names[i]
zip(names,ages)###将两个序列压缩到一起
for name,age in zip(names,ages):
    print name,'is',age,'years old'
name,age=names,ages###在for循环中赋值是按多次赋值，但非for循环中，则是一次性赋值
zip(range(5),xrange(1000000))###zip可以做用于任意长度的序列，即可以应付不等长的序列，当最短序列结束时就停止
###编码迭代
for string in strings:
    if 'xxx' in string:
        index=string.index(string)###search for the string in the list of strings
        strings[index]='[censored]'
index =0
for string in strings:
    if 'xxx' in string:
        strings[index]='[censored]'
    index+=1
for index,string in enumerate(strings):
    if 'xxx' in string:
        strings[index]='[censored]'
###翻滚和排序迭代
sorted([4,3,6,8,3])
sorted('Hello,World!')
reversed('Hello , Wrold!')###返回的是迭代对象
list(reversed('Hello , Wrold!'))
''.join(reversed('Hello,world!'))
###跳出循环
from math import sqrt
for n in range(99,0,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
range(0,10,2)
for x in seq:
    if condition1:continue
    if condition2:continue
    if condition3:continue
    do_something()
    do_something_else()
    do_another_thing()
    etc()
for x in seq:
    if not (condition1 or condition2 or condition3):
        do_something()
        do_something_else()
        do_another_thing()
        etc()
word='dummy'
while word:
    word=raw_input('Please enter a word:')
    #处理word:
    print 'The word was '+ word
word=raw_input('Please enter a word:')
while word:
    #处理word
    print 'The word is ' + word
    word=raw_input('Please enter a word:')
###while True/break
while True :
    word=raw_input('Please enter a word:')
    if not word:break
    #处理word:
    print 'The word was' + word
###循环中的else子句
broke_out=False
for x in seq:
    do_something(x)
    if condition(x):
        break_out=True
        break
    do something_else(x)
if not break_out :
    print "I didn't break out!"
from math import sqrt
for n in range(99,81,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
else:
    print "Didn't find it"
###列表推导式
[x*x for x in range(10)]        
[x*x for x in range(10) if x%3==0 ]    
[(x,y) for x in range(3) for y in range(3)]
result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
result
girls=['alice','bernice','clarice']
boys=['chirs','arnold','bob']
[b+'+'+g for b in boys for g in girls if b[0]==g[0]]
girls=['alice','bernice','clarice']
boys=['chirs','arnold','bob']
letterGirls={}
for girl in grils:
    letterGirls.setdefault(girl[0],[]).append(gril)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]
###pass可以作为占位符使用,在测试中特别有用
if name=='Ralph Auldus Melish':
    print 'Welcome'
elif name=='Enid':
    #还没完
    pass
elif name=='Bill Gates':
    print 'Access Denied'
    
###del删除,不仅会删除对象的引用，还会移除那个名字本身
scoundrel={'age':42,'first name':'Robin','last name':'of Locksley'}
robin=scoundrel
scoundrel
robin
scounderl=None
robin
robin=None         
x=1
del x 
x
x=['Hello','World']
y=x
y[1]='python'
x
del x
y
###exec和eval执行和求值字符串
exec "print 'Hello,World'"###不返回任何对象
from math import sqrt
exec "sqrt=1"
sqrt(4)
from math import sqrt
scope={}###起到放置代码字符串空间作用的字典
exec 'sqrt=1' in scope
sqrt(4)
scope['sqrt']
len(scope)
scope.keys()
print scope
eval(raw_input("Enter an arithmetic expression: "))###用于求值
scope={}
scope['x']=2
scope['y']=3
eval('x*y',scope)
scope={}
exec 'x=2' in scope
eval('x*x',scope)





