##OPERATOR OVERLOADING
#class Student:
#   def __init__(self,m1,m2):
#        self.m1=m1
#        self.m2=m2
#    def __sub__(self,other):
#        

 #       m1=self.m1-other.m1
#        m2=self.m2-other.m2
#        s3=Student(m1,m2)
#        return s3
#s1=Student(56,76)
#s2=Student(32,45)
#s3=s1-s2
#print(s3.m1)
#print(s3.m2)
#print(s3)

#n=int(input("enter the size of the array : "))
#lst=list(map(int,input("enter the integer\elements : ").strip().split()))[:n]
#print(lst)
#lst.reverse()
#print("the list after reversing is : ")
#print(lst) 
#class Computer:
 #   def __init__(self,cpu,ram):
#      self.cpu=cpu
#      self.ram=ram
#    def config(self):
#       print("configaration is ",self.cpu,self.ram)
#com1=Computer("i5",16)
#com2=Computer("rayon")
#com1.config()
#com2.config()



#class Addition:
#    def __init__(self,f,s):
#        self.first=f
#        self.second=s 
#    def add(self):
#        print("first number is : ",self.first)
#        print("second number is : ",self.second)
#        print("the sum is : ",self.answer)
#    def calc(self):
 #       self.answer=self.first+self.second
#obj1=Addition(100,200)
#obj1.calc()
#obj1.add()
##INNER CLASS
#class Student:
#    def __init__(self,name,rollno):
#        self.name=name
#        self.rollno=rollno
 #       self.lap=self.Laptop()
 #   def show(self):
 #        print(self.name)
 #        print(self.rollno)
 #   class Laptop:
 #       def __init__(self) :
 #           self.brand="hpu"
 #           self.cpu="i5"
 ##           self.ram="8tb"
 #       def show(self):
  #          print(self.brand)
  #          print(self.cpu)
  #          print(self.ram)

#s1=Student("navin",222)
#s2=Student("jenny",33) 
#s1.show()
#s2.show()
#lap1=Student.Laptop()
#lap1.show()
#INHERITENCE IN PYTHON
#class A:
#   def __init__(self):
#      print("in a in it")
#   def feature(self):
 #     print("feature 1 working")
 #  def feature1(self):
 #     print("feature 2 working")
#class B(A):
#    def __init__(self): 
#      print("in b in it")
#    def feature2(self):
#      print("feature 3 working")
#    def feature3(self):
#      print("feature 4 working")
#class C(B):
#   def __init__(self):
#      print("in c in it")
#      super().feature2 ( )
#a1=C()
#POLYMORPHISM
#class Pycharm:
#    def execute(self):
#        print("compiling")
#        print("running")
#class Myeditor:
#    def execute(self):
#        print("spell check")
#        print("conventional check")
#        print("running")
#        print("compiling")
#class Laptop:
#    def code(self,ide):
#       ide.execute()
#ide=Myeditor()
#lap=Laptop() 
#lap.code(ide)
#METHOD OVERRIDING
#class A:
#    def show(self):
#        print("in A show")
#class B(A):
#    def show(self):
#        print("in B show")
#        super().show ()
#a1=B()
#a1.show()
#ABSTRACTION IN PYTHON
#from abc import ABC,abstractmethod
#class Computer(ABC):-> class becomes abstract
    #def process(self):
    # pass->abstract method
    #def public(self):
    #   print("i am in public")
#class Laptop(Computer):
#   def process(self):
#      print("hi")
#l1=Laptop()
#l1.process()
#c1=Computer()
#c1.public()
#ITERATORS
#nums=[1,2,3,4]
#it=iter(nums)
#print(it.__next__())
#print(it.__next__())
#print(next(it)) 
#EXCEPTIONAL HANDLING IN PYTHON
#a=5
#b=2
#try:
#    print(a/b-2)
#    k=int(input("enter the number : "))
#    print(k)
#except ZeroDivisionError as e:
#  print("you cannot divide by zero + ",e)
#except ValueError as e:
#   print("invalid type",e)
#except Exception as e:
#   print("Exception",e)
#finally:  
#  print("bye")
#THREADS IN PYTHON
#from time import sleep
#from threading import Thread
#class Hello(Thread):
#   def run(self):
#      for i in range(0,5 ):
#         print("hello") 
#         sleep(0.5)

#class Hi(Thread):
#   def run(self):
#      for i in range(0,5):
#         print("hi") 
#         sleep(0.5)
#t1=Hello()
#t2=Hi()
#t1.start()
#sleep(0.2)
#t2.start()
#t1.join()
#t2.join()
#print("bye")
#list=[3,4,5,61,2,6,8,45]
#print(sorted(list))
#import numpy as np
#arr=np.array(((1,2),
#             [3,4]),dtype=np.float64)
#brr=np.array([[3,2],
#             [5,6]],dtype=np.float64)
#sum1=np.add(arr,brr)
#np.prod(var) gives the product of corresponding list
#print(sum1)
#print(arr.sum())
#print(np.sqrt(arr))
#print(arr.T)
#print(brr.dtype)
#print(arr.shape)#gives no.of rows and columns in an array
#print(arr.size)#how many elements in the matrix
#np.fromiter gives the one dimensional array
#import numpy as np
#var="geeksforgeeks"
#arr=np.fromiter(var,dtype="U2")
#print(arr)
#s=np.arange(1,20,4)
#print(s)
#s=np.linspace(1,20,5)
#print(s)
#a=np.empty([2,3],dtype=int)
#print(a)#creates matrix of zeros without any rules
#a=np.zeros([4,3],dtype=int)
#print(a)
#d=np.empty([3,3],dtype=int)
#print(d)
#print(arr.max(axis=1))#gives max in rows
#max gives row wise and min gives column wise 
#ASCII value
#s=input("enter the string : ")
#for i in s:
#   print(ord(i),"is the ascii of ",i)
##PANDAS
import datetime
import pandas as pd
#data={"name":["sasi","priya","vijaya","charan","prasad"],
#     "age":[20,21,22,23,34],
#      "Address":["delhi","bombay","andra","telengana","kerala"],
#       "Qualification":["bba","bce","cse","btech","mca"] }
#df=pd.DataFrame(data)
#print(df[["name","Qualification","Address"]])
#print("---------------")
#print(df.shape)
# import numpy as np
# dict={"first score":[100,90,80,np.nan,95],
#       "Second score":[30,45,np.nan,667,78],
#       "Third score":[12,23,4,56,66]}
# df=pd.DataFrame(dict)
# print(df)
# print(df.fillna(50))
# print(df.dropna())
#for i,j in df.iterrows():
 #   print(i,j)
#columns=list(df)
#for i in columns:
#    print(df[i])
#print(df.index)
#data={"name":["avaery","john","jonas","jordan"],
#      "Team":["boston","boston","bostan","boston"],
#      "number":[0.0,30.0,8.0,12.0,11.0]}
#ser=pd.Series(data["name"])
#print(ser)
#data=np.array(["g","e","e","k","s"])
#ser=pd.Series(data,index=[10,11,12,13,14])
#print(ser)

##IF THE INPUT IS FROM THE USER THEN IT IS NOT NECESSARY TO USE THE METHOD INITIALISE
##BUT WHEN IT IS FROM USER(INPUT)THEN INITIALISE METHOD ID NECESSARY
##__str__(). that is used to define how a class object should be represented as a string

##if you dont have any method name then to print the function using print(object name)
# class Base:
#     def __init__(self):
#         self.a=10
# class Student(Base):
#     def __init__(self):
#         Base.__init__(self)
#         b=10
#         print(self.a+b)
# sasi=Student()
# print(sasi)
#if we use __init__ then we can use the varaible acroos the code using the concept of inheritence
# to define a private member prefix the member name with double underscore “__”.
#private variables cannot be inherited
#we can even access the varaibles in method overloading using for loop
#write for any name in (objects):
#anyname.method_names
# class India():
#     def capital(self):
#         print("india is the populated country")
#     def lan(self):
#         print("most of the indians speak hindi")
#     def tyr(self):
#         print("the capital city of india is new delhi ")
# class Usa():
#     def capital(self):
#         print("washington is the captial of america")
#     def lan(self):
#         print("english is the primary language")
#     def tyr(self):
#         print("the capital city of usa is washington dc")
# obj1=India()
# obj2=Usa()
# for yy in (obj1,obj2):
#     yy.capital()
#     yy.lan()
#     yy.tyr()
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
  
# obj_ind = India()
# obj_usa = USA()
  
# func(obj_ind)
# # func(obj_usa)
#static varaibles should be called by class names and not by the method names
# a="geeksforgeeks"
# String=a[0:2]+"p"+a[3:]
# print(String)
#A string can be left() or center(^) justified with the use of format specifiers, separated by a colon(:).  
# import random
# import string
# def rand(size):
#     generate_pass="".join([random.choice(string.ascii_letters+string.digits)
#                            for n in range(size)])
#     return generate_pass
# password=rand(10)
# print(password)
#split is used to write code in one line and to assaign the value respectively
#REVERSING A STRING
# s="sasi"
# y=list(s)
# a=" "
# y=y[::-1]
# for i in y:
#     a+=i
# print(a)
1222311
#output(1,1(2,3)(3,1)(1,2))
# x=input("Enter the number : ")
# s=list(x)
# for i in range(len(s)-1):
#   c=1
#   if(s[i]==s[i+1]):
#     c+=1
#   print(s[i],c)
# else:
#   print(s[i],c)
# import sys
# for line in sys.stdin:
#     if "q"==line.rstrip():
#         break
#     print(f"Input:{line}")
# print("Exit")
# sys.stdout.write("Geeks")

# txt="    banana,,,,,,sqqqqqqqqq.......   "
# x=txt.rstrip()
# print("of all fruits ",x,"is my favourite")
# import emoji
# def main():
#     try:
#           x=input("Text : ")
#           print(emoji.emojize(x))
#     except EOFError:
#         print("Out of loop")
# if __name__=="__main__":
#     main()
# print(emoji.emojize(':beer_mug:'))
# print(emoji.demojize("😺"))
# import pyfiglet
# x=input("Input : ")
# result = pyfiglet.figlet_format(x,font="alphabet")
# print(result)
#reddysasipriya2005@gmail.com
# import re
# email=input("Whats the email : ").strip()
# if re.search(r"^\w+@(\w+\.)?\w+\.{edu|com|gov}$",email,re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")
# class Base:
#     def __init__(self):
#         self.a="Geeks for geeks"
#         self.__c="Geeks for geeks"
#         print(self.__c ,"is")
# class Derived(Base):
#     def __init__(self):
#        Base.__init__(self)
#        print(self.__c)
# obj1=Base()
# print(obj1.a)

