#n = int(input("enter the number of days : "))
#print("years",(n//365))
#print("days",(n%365))

#import math
#n = int(input("enter the radians : "))
#print(math.sin(math.radians(n)))

#n = (input("enter a number : "))
#reverse=n[::-1]
#if(n==reverse):
    #print("it is a palindrome")
#else:
    #print("it is not a palindrome")

#n = int(input("enter the temperature in degrees : "))
#print(n,"saturday")
#print(3+n,"sunday")
#print(n-5,"monday")
#print(n+2,"tuesday")
#print(n+6,"wednesday")
import pandas as pd
import numpy as np
data1={"name":["jai","sasi","gaurav","nuj"],
      "Age":[10,15,14,12],
      "gender":['M','F','M','M'],
      "Address":["bombay","delhi","kanpur","delhi"]}
data2={"name":["sasi","charan","vijaya","prasad"],
       "Age":[11,12,12,33],
       "gender":["f","m","f","m"],
       "Address":["bhopal","bombay","delhi","odissa"]}
df1=pd.DataFrame(data1,index=[0,1,2,3])
df2=pd.DataFrame(data2,index=[4,5,6,7])
ss=[df1,df2]
print(pd.concat(ss))