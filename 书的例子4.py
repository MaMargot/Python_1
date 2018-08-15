# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:34:09 2018

@author: MaMargot
"""

fibs=[0,1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])
fibs
num=input('How many Fibonacci numbers do you want:')
for i in range(num-2):
    fibs.append(fibs[-2]+fibs[-1])
print fibs
num=input('How many numbers do you want?')
print fibs(num)
import math 
x=1
y=math.sqrt
callable(x)###判断函数是否可以调用
callable(y)
def hello(name):
    return 'Hello,'+name+'!'
print hello('world')
print hello('Gumby')
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
fibs(10)
fibs(15)
def square(x):
    'Calculates the square of the number x.'
    return x*x
callable(square)
square._doc_###访问文档字符串，_doc_是函数属性
help(square)###也可以获得文档字符串的信息
def test():
    print 'This is printed'
    return
    print 'This is not'
test()
def try_to_change(n):
    n='Mr.Gumby'
name='Mrs.Entity'
try_to_change(name)
name
n=name###这句话的作用基本上等于传参数
n='Mr.Gumby'###在函数内部完成
name
def change(n):
    n[0]='Mr.Gumby'
names=['Mrs.Entity','Mrs.Thing']
change(names)
names
names=['Mrs.Entity','Mrs.Thing']
n=names#再来一次，模拟传参行为      引用的是同个列表
n[0]='Mr.Gumby'
names
names=['Mrs.Entity','Mrs.Thing'] 
n=names[:]###序列做切片时，得到的是副本
n is names
n==names
n[0]='Mr.Gumby'
names
n
change(names[:])###  !!!
names
storage={}
storage['first']={}
storage['middle']={}
storage['last']={}
me=['Magnus Lie Hetland']
storage['first']['Magnus']=me
storage['middle']['Lie']=me
storage['last']['Hetland']=me
storage['middle']['Lie']
my_sister='Annie Lie Hetland'
storage['first'].setdefault('Annie',[]).append(my_sister)
storage['middle'].setdefault('Lie',[]).append(my_sister)
storage['last'].setdefault('Hetland',[]).append(my_sister)
storage['first']['Annie']
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
storage={}
init(storage)
storage
def lookup(data,label,name):
    return data[label].get(name)
lookup(storage,'middle','Lie')
def store(data,full_name):
    names=full_name.split(' ')
    if len(names)==2: names.insert(1,' ')
    labels='first','middle','last'
    for label,name in zip(labels,names):
       people=lookup(data,label,name)
       if people:
           people.append(full_name)
       else:
           data[label][name]=[full_name]
Mynames={}
init(Mynames)
store(Mynames,'Magnus Lie Hetland')
lookup(Mynames,'middle','Lie')
store(Mynames,'Robin Hood')
store(Mynames,'Robin Locksley')
lookup(Mynames,'first','Robin')
store(Mynames,'Mr. Gumby')
lookup(Mynames,'middle',' ')
def inc(x): return x+1
foo=10
inc(foo)
def inc(x): x[0]=x[0]+1
foo=[10]
inc(foo)
foo
def hello1(greeting,name):
    print "%s,%s!"%(greeting,name)
def hello2(name,greeting):
    print "%s,%s!"%(name,greeting)
hello1('Hello','World')
hello2('Hello','World')
###关键参数和默认值
hello1(greeting='Hello',name='World')
hello1(name='World',greeting='Hello')
hello2(greeting='Hello',name='World')
store('Mr.Brainsample',10,20,13,5)
store(patient='Mr.Brainsample',hour=10,minute=20,day=13,month=5)###关键参数
def hello_3(greeting='Hello',name='World'):
    print '%s,%s!'%(greeting,name)
hello_3()
hello_3('Greeting')
hello_3('Greeting','universe')
hello_3(name='Gumby')
def hello_4(name,greeting='Hello',punctuation='!'):
    print "%s,%s%s"%(name,greeting,punctuation)
hello_4('Mars')
hello_4('Mars','Howdy')
hello_4('Mars','Howdy','...')
hello_4('Mars',punctuation='.')
hello_4('Mars',greeting='Top of the morning to ta')
hello_4
###收集参数
def print_params(*params):
    print params
print_params('Testing')###由于*存在，参数变成了元组,将所有值放置在同一个元组中
print_params(1,2,3)
def print_params2(title,*params):
    print title
    print params
print_params2('params',1,2,3)
print_params2('nothing')
print_params2('Hmm....',something=42)
def print_params3(**params):
    print params
print_params3(x=1,y=2,z=3)###返回的是字典
def print_params4(x,y,z=3,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar
print_params4(1,2,3,5,6,7,fool=1,bar=2)
print_params4(1,2)
def store(data,*full_names):
    for full_name in full_names:
        names=full_name.split()
        if len(names)==2 : names.insert(1,' ')
        labels='first','middle','last'
        for label,name in zip(labels,names):
            people=lookup(data,label,name)
            if people:
                people.append(full_name)
            else:
                data[label][name]=[full_name]
d={}
init(d)
store(d,'Han Solo')
store(d,'Luke Skywalker','Anakin Skywalker')
lookup(d,'last','Skywalker')
###反转过程
def add(x,y): return x+y
params=(1,2)
add(*params)###在调用时使用*，分配元组参数
params={'name':'Sir Robin','greeting':'well met'}
hello_3(**params)###同理使用**，分配字典参数
def with_stars(**kwds):
    print kwds['name'],'is',kwds['age'],'year old'
def without_star(kwds):
    print kwds['name'],'is',kwds['age'],'year old'
args={'name':'Mr.Gumby','age':42}
with_stars(**args)
without_star(args)
###星号只在定义(允许使用不定数目的参数)或调用(分割字典或序列)函数时才有用
def foo(x,y,z,m=0,n=0):
    print x,y,z,m,n
def call_foo(*args,**kwds):
    print 'Calling foo!'
    foo(*args,**kwds)

def story(**kwds):
    return 'once upon a time. there was a '\
           '%(job)s called %(name)s.'%kwds
def power(x,y,*others):
    if others:
        print 'Received redundant parameter:',others
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for step>0'
    if stop==None:               ###如果没有为stop提供值......
        start,stop=0,start       ###指定参数
    result=[]
    i=start                      ###计算start的索引
    while i< stop:               ###直到计算到stop的索引
        result.append(i)         ###将索引添加到result内......    
        i+=step                  ###将step(>0)增加索引i......
    return result
print story(job='king',name='Gumby')
print story(name='Sir Robin',job='brave knight')    
params={'job':'language','name':'Python'}
print story(**params)
del params['job']
print story(job='stroke of genius',**params)
power(2,3)
power(3,2)
power(y=3,x=2)
params=(5,)*2
params
power(*params)
power(3,3,'Hello world')
interval(10)
interval(1,5)
interval(3,12,4)
power(*interval(3,7))
###作用域
x=1
scope=vars()###返回额字典是不可修改的,此处返回的字典是命名空间、作用域
scope['x']
scope['x']+=1
x
def foo(): x=42
x=1
foo()
x
def output(x): print x
x=1
y=2
output(y)
def combine(parameter): print parameter+external
external='berry'
combine('Shrub')
def combine(parameter): print parameter+globals()['parameter']
parameter='berry'
combine('Shrub')###globals()与locals()分别返回全局变量和局部变量的字典
x=1
def change_global():
    global x ###声明该变量为全局变量
    x=x+1
change_global()
x
def foo():  ###函数嵌套
    def bar():
        print 'Hello,World'
    bar()
def multiplier(factor):
    def multiplyByfactor(number):
        return number*factor
    return multiplyByfactor
double=multiplier(2)
double(5)
double(3)
tripe=multiplier(3)
tripe(3)
multiplier(5)(4)

###递归
###1.阶乘和幂
def factorial(n):
    result=n
    for i in range(1,n):
        result*=i
    return result
def factorial(n):
    if n==1:
        result=1
    else:
        return n*factorial(n-1)
def power(x,n):
    result=1
    for i in range(n):
        result*=x
    return result
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
###2.二元查找
def search(sequence,number,lower=0,upper=None):
    if upper is None:upper=len(sequence)-1
    if lower==upper:
        assert number==sequence[upper]
        return upper
    else:
        middle=(lower+upper)//2
        if number>sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)
seq=[34,67,8,123,4,100,95]
seq.sort()
seq
search(seq,34)
search(seq,100)

###
map(str,range(10))###可以将一个序列中的值传递给函数
###filter()可以基于布尔值的函数对元素进行过滤
def func(x):
    return x.isalnum()
seq=['foo','x42','?!','****']
filter(func,seq)
filter(lambda x:x.isalnum(),seq)###可以创建短小函数
number=[72,101,108,108,111,44,32,119,111,114,108,100,33]
reduce(lambda x,y:x+y,number)


###多态和方法
#不要这么做
def getPrice(object):
    if isinstance(object,tuple):###进行类型/类的检查
        return object[1]
    else:
        return magic_network_method(object)
#不要这样做
def getPrice(object):
    if isinstance(object,tuple):
        return object[1]
    elif isinstance(object,dict):
        return int(object['price'])
    else:
        return magic_network_method(object)
object.getPrice()        
'abc'.count('a')
[1,2,'a'].count('a')
from random import choice
x=choice(['Hello,World!',[1,2,'e','e',4]])        
x.count(x)        
1+2        
'Fish'+'license'        
def add(x,y):
    return x+y
add(1,2)        
add('Fisher','license')        
def length_message(x):
    print "The lenght of ",repr(x),"is",len(x)
length_message('Fnord')        
length_message([1,2,3])  
###闭包      
o=OpenObject()###创建对象，并绑定类
o.setName('Sir Lacncelot') 
o.getName
globalName
globalName='Sir Gumby'
o.getName()
o1=OpenObject()
o2=OpenObject()
o1.setName('Robin Hood')
o2.getName()
c=ClosedObject()
c.setName('Sir Lancelot')
c.getName()
r=ClosedObject()
r.setName('Sir Robin')
r.getName()        
###创建类
__metaclass__=type #确定使用新式类,该步放置赋值语句
class Person:
    def setName(self,name):#对于对象自身的引用
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,World! I'm %s."%self.name 
foo=Person()  #方法/绑定，将它们的第一个参数绑定到所属的实例上      
bar=Person()    
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet() #等价于Person.greet(foo)
bar.greet()
foo.name###特性是可以在外部访问的
bar.name='Yoda'
bar.greet()
class Class:
    def method(self):
        print 'I have a self'
def function():
    print "I don't..."
instance=Class()
instance.method()
instance.method=function #将特性绑定到普通函数上
instance.method()
class Bird:
    Song='Sqaawk!'
    def sing(self):
        print self.Song
bird=Bird()
bird.sing()
birdsong=bird.sing()###绑定在bird.sing()上，还是对self参数的访问
birdsong
c.name
c.name='Sir Gumby'
c.getname()
class Secretive:
    def __inaccessible(self): #在名字前加上双下划线，可是外部无法访问特性
        print "Bet you can't see me ..."
    def accessible(self):
        print "The secret message is: "
        self.__inaccessible()
s=Secretive()
s.__inaccessible()
s.accessible()
Secretive._Secretive__inaccessible#在类的内部定义中，所有双下划线开始的名字都被翻译成前面加上单下划线和类名的格式
s._Secretive__inaccessible()
def foo(x): return x*x
foo=lambda x:x*x
###类的命名空间
class C:
    print 'Class C being defined...'
class MemberCounter:
    members=0
    def init(self):
        MemberCounter.members+=1
ml=MemberCounter()    
ml.init()
MemberCounter.members
m2=MemberCounter()
m2.init()
MemberCounter.members
ml.members
m2.members
ml.members='Two'
ml.members
m2.members
###指定超类
class Filter:
    def init(self):
        self.blockd=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter): #SPAMFilter是Filter的子类
    def init(self): #重写Filter超类中的init方法
        self.blocked=['SPAM']
f=Filter() #Filter是个用于过滤序列的通用类
f.init()
f.filter([1,2,3])#事实上不能过滤任何东西，用处在于它可以作为其他类的基类
s=SPAMFilter()
s.init()
s.filter(['SPAM','SPAM','SPAM','SPAM','eggs','bacon','SPAM'])
issubclass(SPAMFilter,Filter)###查看一个类是否另一个的子类
issubclass(Filter,SPAMFilter)
SPAMFilter.__bases__#查看已知类的基类
Filter.__bases__
s=SPAMFilter()
isinstance(s,SPAMFilter)#查看一个对象是否是一个类
isinstance(s,Filter)
isinstance(s,str)
s.__class__#查看对象属于哪个类
type(s)#如果使用__metaclass__=type或从object集成的方式来定义新式类，可以使用type()来查看实例的类
###多个超类
class Calculator:
    def calculator(self,expression):
        self.value=eval(expression)
class Talker:
    def talker(self):
        print 'Hello,my value is',self.value
class TalkerCalculator(Calculator,Talker):###注意：如果一个方法从多个超类继承（即多个相同名字的不同方法），要注意超类的顺序，在class语句中，先继承的类中的方法会重写后继承的类中的方法。(如class TalkerCalculator(Talker，Calculator):pass)
    pass
tc=TalkerCalculator()    
tc.calculator('1+2*3')       
tc.talker()
hasattr(tc,'talker')#检查是否存在特性
hasattr(tc,'Fnord')
callable(getattr(tc,'talker',None))#检查特性是否能被调用，getattr()用来获取特性，并提供默认值
callable(getattr(tc,'Fnord',None))
setattr(tc,'name','Mr.Gumby')#设置对象的特性
tc.name
tc.__dict__#查看对象内所有存储的值



