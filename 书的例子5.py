# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 21:45:29 2018

@author: MaMargot
"""

###异常
1/0
raise Exception #Exception内建的异常集类,普通异常，raise引发异常
raise Exception ('hyperdrive overload')#附带错误信息
import exceptions #内建异常模块和内建的命名空间
dir(exceptions) #列出模块内容
raise(ArithmeticError)
######################一些内建异常########################
#Exception 所有异常的基类
#AttributeError 特性引用或赋值失败时引发
#IOError 试图打开不存在文件（包括其他情况）时引发
#Index 在使用序列中不存在的索引时引发
#KeyError 在使用映射中不存在的键时引发
#NameError  在找不到名字（变量）时引发
#SyntaxError 在代码为错误形式时引发
#TypeError 在内键操作或者函数应用于错误的类型的对象时引发
#ValueError 在内键操作或者函数应用于正确的类型
#ZeroDivisionError  在除法或者模除的第二个参数为时引发
##########################################################
class SomeCustomException(Exception): #自定义异常类
    pass #只要确保从Exception类继承（不管是间接还是直接，也就是说继承其他的内键异常类也是可以的）
x=input("Enter the first number: ")
y=input("Enter the second number: ")
print x/y
try:#捕抓异常
    x=input("Enter the first number: ")
    y=input("Enter the second number: ")
    print x/y
except ZeroDivisionError :
    print "The second number can't be zero!"
class MuffledCalculator:
    muffled=False
    def calc(self,expr):
        try:#捕抓异常
            return eval(expr)
        except ZeroDivisionError :
            if self.muffled:#此处为屏蔽机制
              print "Division by zero is illgal"
            else:
                raise#传递异常
calculator=MuffledCalculator()
calculator.calc('10/2')
calculator.calc('10/0')
calculator.muffled=True #打开屏蔽机制
calculator.calc('10/0')
try:#捕抓异常
    x=input("Enter the first number: ")
    y=input("Enter the second number: ")
    print x/y
except ZeroDivisionError :
    print "The second number can't be zero!"
except TypeError: #多个except
    print "That wasn't a number,was it?"
try:
    x=input('Enter the first number:')
    y=input('Enter the second number:')
    print x/y
except (ZeroDivisionError,TypeError,NameError):###用一个块捕抓多个类型的异常
    print "Your numbers were bogus"
try:#捕获对象
    x=input('Enter the first number:')
    y=input('Enter the second number:')
    print x/y
except (ZeroDivisionError,TypeError),e:#访问异常对象本身，就算捕获到多个异常，也只需想except子句提供一个参数(一个元组)
    print e
try: #捕获所有异常
    x=input('Enter the first number:')
    y=input('Enter the second number:')
    print x/y
except: #用except Exception,e更好些
    print 'Something wrong happened'
try:
    print 'A simple task'
except:
    print 'What?Something went wrong?'
    else:
print 'Ah...It went as planned'
while True:
    try:
       x=input('Enter the first number:')
       y=input('Enter the second number:')
       value=x/y
       print 'x/y is',value
    except:
       print 'Invalid input.Please try again'
    else:
       break
while True:
    try:
        x=input('Enter the first number:')
        y=input('Enter the second number:')
        value=x/y
        print 'x/y is',value
    except Exception,e:
        print 'Invlid input:',e
        print 'Please try again'
    else:
        break
x=None 
try:
    1/0
finally:#用在可能的异常后进行清理,finally子句是一定会被执行，不管try子句中是否发生异常（用于关闭文件或者网络嵌接字时会非常有用）
    print 'Cleaning up'
    del x#若x没有被赋值，此处将出现异常，该异常时无法捕获的
try:#组合
    1/0
except NameError:
    print "Unknown Variable"
else:
    print "That went well"
finally:
    print "Cleaning up"
#异常与函数
def faulty():
    raise Exception('Something is wrong')
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handled'
ignore_exception()
handle_exception()
def describePerson(person):
    print 'Description of ',person['name']
    print 'Age ',Person['age']
    if 'occupation' in person:
        print 'Occupation:',person['occupation']
def describePerson(person):
    print 'Description of ',person['name']
    print 'Age ',Person['age']
    try:
        print 'Occupation:'+person['occupation']
    except KeyError: pass
try:
    obj.write
except AttributeError:
    print 'The object is not writeable'
else:
    print 'The object is writeable'
        
###魔法方法、属性、迭代器
class NewStyle(object):#新式类
    more_code_here
class OldStyle(object):#旧式类，若将__metaclass__=type放置于开始，则为新式类
    more_code_here
##构造方法
f=FooBar()
f.init()
f=FooBar()
__metaclass__=type
class FooBar:
    def __init__(self):#区别于init：当一个对象被创建后，会立即调用构造方法
        self.somvar=42
f=FooBar()
f.somvar
class FooBar:
    def __init__(self,value=42):
        self.somvar=value
f=FooBar()
f.somvar
f=FooBar('This is a constructor argument')
f.somvar
#重写一般方法和特殊的构造方法
class A:
    def hello(self):
        print "Hello,I'm A."
class B(A):
    pass
a=A()
b=B()
a.hello()
b.hello()
class B(A):
    def hello(self):
        print "Hello,I'm B"
b=B()
b.hello()
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry=False
        else:
            print 'No,thanks'
b=Bird()
b.eat()
b.eat()
class SongBird(Bird):
    def __init__(self):
        self.sound='Squawk!'
    def sing(self):
        print self.sound
sb=SongBird()    
sb.sing()
sb.eat()
#调用未绑定的超类构造方法
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)###self参数自动banding到实例上
        self.sound='Squawk!'
    def sing(self):
        print self.sound
sb=SongBird()            
sb.sing()
sb.eat()
sb.eat()
#使用super函数，即使类已经继承多个超类，它也只需要使用一次super函数，但要保证所有的超类的构造方法都是用了super函数
__metaclass__=type #super只在新类中起作用
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry=False
        else :
            print 'No.thanks'
class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()#必须在新式类中
        self.sound='Squawk!'
    def sing(self):
        print self.sound
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()
#成员访问，基本的序列和映射规则
def checkIndex(key):
    """
    所给的键是能接受的索引吗？
    为了能被接受，键应该是一个非负的整数。如果它不是一个整数，会引发TypeError异常；
    如果它是个负数，则会引发一个IndexError异常。
    """
    if not isinstance(key,(int,long)):raise TypeError
    if key<0 :raise IndexError
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        """
        初始化算术序列
        初始值---序列中的第一个值
        步长---两个相邻之间的差别
        改变---用户修改的值的字典
        """
        self.start=start#初始化开始值
        self.step=step#初始化步长值
        self.changed={}#没有项被修改
    def __getitem__(self,key):
        """
        Get an item from the arithnetic sequence.
        """
        checkIndex(key)
        try :return self.changed[key] #修改了吗？
        except KeyError: #否则.....
             return self.start+key*self.step #...计算值
    def __setitem__(self,key,value):
        """
        修改算术序列中的一个项
        """
        checkIndex(key)
        self.changed[key]=value #保存更改后的值
s=ArithmeticSequence(1,2)
s[4]
s[5]
s[4]=2
s[4]
s[5]
del s[4]
s["four"]
s[-45]
class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.count=0
    def __getitem__(self,index):
        self.count+=1
        return super(CounterList,self).__getitem__(index)
c1=CounterList(range(10))
c1
c1.reverse()
c1
del c1[3:6]
c1
c1.count
c1[4]+c1[2]
c1.count
#属性
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,*size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
r=Rectangle()
r.width=10
r.height=5        
r.getSize()
r.setSize(150,100)
r.getSize()
__metaclass__=type
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
    size=property(getSize,setSize)#用于创建属性,四个参数fget，fset，fdel，doc--
r=Rectangle()
r.width=10
r.height=5        
r.size
r.size=150,100
r.size
#静态方法和类成员方法
__metaclass__=type
class Myclass:
    def smeth():
        print 'This is a static method'
    smeth=staticmethod(smeth)
    def cmeth(cls):
        print 'This is a class method of ',cls
    cmeth=classmethod(cmeth)
r=Myclass()        
r.smeth()
r.cmeth()
Myclass.smeth()###没有实例化类
Myclass.cmeth()
__metaclass__=type
class Myclass:
    @staticmethod###修饰器，能够对任何可调用的对象进行包装，多个修饰器在应用时的顺序与指定的顺序相反
    def smeth():
        print 'This is a static method'
    @classmethod
    def cmeth(cls):
        print 'This is a class method of ',cls
Myclass.smeth()###没有实例化类
Myclass.cmeth()
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self,name,value):
        if name=='size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value###一个特殊方法，包括了一个字典，该字典里面是所有实例的属性
    def __getattr__(self,name):
        if name=='size':
            return self.width,self.height
        else :
            raise AttributeError
#迭代器规则
class Fibs:
    def __init__(self):
        self.a=0
        self.b=0
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):#实际上返回迭代器本身
        return self            
fibs=Fibs()
for f in fibs:
    if f > 1000 :
        print f
        break
it=iter([1,2,3])
it.next()
it.next()     
#从迭代器得到序列      
class TestIterator :
    value=0
    def next(self):
        self.value+=1
        if self.value >10 : raise StopIteration
        return self.value
    def __iter__(self):
        return self
it=TestIterator()
list(it)#使用list构造方法显式地将迭代器转化为列表        
#生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element ###任何包含yield语句的函数称为生成器
nested=[[1,2],[3,4],[5]]
for num in flatten(nested):
    print num  ###每次产生多个值，但每次产生一个值(使用yield语句)，函数就会被冻结：即函数停留在那点等待被激活             
flatten(nested)            
list(flatten(nested))            
g=((i+2)**2 for i in range(2,27))###生成器表达式
g.next()            
sum(i**2 for i in range(10))###可以在当前的圆括号内直接使用
#递归生成器
def flatten(nested):
    try:
        for sublist in nested:
             for element in flatten(sublist):
                 yield element
    except TypeError:###函数被告知展开一个元素时，会引发TypeError异常
        yield nested
list(flatten([[[1],2],3,4,[5,[6,7]],8]))
[1,2]+[3,4]           
[1,2]+(' ')          
def  flatten(nested):###在生成器的开始处添加一个检查语句
    try : 
        #不要迭代类似字符串的对象
        try:nested+' '
        except TypeError: pass
        else: raise TypeError
        for sublist in nested :
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
list(flatten( ['foo',['bar',['baz']]]))               
#通用的生成器
def simple_generator():###生成器由两部分组成：生成器的函数和生成器的迭代器
    yield 1
simple_generator
simple_generator()            
#生成器方法，使用send方法只有在生成器被挂起后才有意义，即在yield函数第一次被执行之后
def repeater(value):
    while True:
          new=(yield value)
          if new is not None: value=new
r=repeater(42)
r
r.next()###next被调用时，yield方法返回None
r.send('Hello,World!')###send方法向函数发送值
r.next()
###throw方法，用于在生成器内引发一个异常（在yield表达式中）
###close方法，用于停止生成器，产生一个GeneratorExit异常，且在close方法被调用后再通过生成器生成一个值则会导致RuntimeError异常
#模拟生成器
result=[]
reuslt.append(some_expression)###替代yield some_expression
def flatten(nested):
    result=[]
    try:
        #不要迭代类似字符串的对象
        try: nest+''
        except TypeError : pass
        else:raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
#八皇后问题









