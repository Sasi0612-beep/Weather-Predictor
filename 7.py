#n = int(input("enter  a number : "))
#y=str(n)
#x=''
#for i in y:
#    x=i+x
#print("the reverse of number : ",x)

#x =str(input("enter the name : "))
#z = str(x)
#y = ""
#for i in z:
#    y=i+y
#print(y)

#n=int(input("enter no of rows : "))
#for i in range(0,n):
#    for j in range (0,i):
 #       print("*",end=" ")
 #   print("*")

#n = int(input("enter no.of rows : "))
#for i in range(1,n+1): 
 #   for j in range(1,i):
 #        print(j,end=" ")
 #   print(i) 

#n = int(input("enter no.of rows : "))
#for i in range(0,n):
  #  for j in range(0,n-i):
 #       print("*",end=" ")
 #   print("*")

#n = int(input("enter no.of rows : "))
#for i in range(1,n+1):
  #  for j in range(1,i+1):
   #     print("*",end=" ")
   # print(i)


#n = int(input("enter a number : "))
#oddtotal=0
#eventotal=0
#for i in range(1,n+1):
#    print(i)
#    if(i%2==0):
 #          print("the given number is even number",i)
 #          oddtotal=oddtotal+1
  #         print("total even numbers=",oddtotal)
 #   else:
 #       print("the number is odd number",i)
  #      eventotal=eventotal+1
   #     print("total odd numbers= ",n-oddtotal)
#print(" total no.of odd numbers = ",n-oddtotal)

#n = int(input("enter a no.of rows : "))
#for i in range(1,n+1):
 # for j in range(1,n-i-2):
  #  print("",end="")
  #for j in range(1,i):
    #print(j,end=" ")
  #print(i)

#for i in range(97,123):
  #print(chr(i),end=" ")

#n=int(input("enter no.of rows : "))
#for i in range(0,n):
 # for j in range(0,n-i-1):
  #  print(" ",end=" ")
  #print("*")

#n = int(input("enter a number : "))
#i=1
#while(i<=n):

#n = str(input("enter the string : "))
#x=len(n)
#print(x)
#if(x<5):
#  print("invalid password")
#else:
#  print("valid password")
# x,y,z = (input("Enter the number : ").split())
# print("x = ",x)
# print("y = ",y)
# print("z = ",z)
# m=x*y*z
# print(m)
# a,b,c=input("Enter the remainder values : ").split()
# print("a = ",a)
# print("b = ",b)
# print("c = ",c)

#CHINESE REMAINDER THEORM
  
# a=[3,4,5]
# b=[2,3,2]
# ab=1
# c=[]
# d=[]
# for i in range(len(a)):
#     ab=ab*a[i]
# a1=int(ab/a[0])
# a2=int(ab/a[1])
# a3=int(ab/a[2])
# c.append(a1)
# c.append(a2)
# c.append(a3)
# print(c,"values of z1,z2,z3")
# def inverse(n,m):
#     for i in range(1,m+1):
#         if((n*i)%m==1):
#             print(i)
#             return i
# x=inverse(20,3)
# y=inverse(15,4)
# z=inverse(12,5)
# d.append(x)
# d.append(y)
# d.append(z)
# print(d,"inverse values")
# chinese=(a1*b[0]*x+a2*b[1]*y+a3*b[2]*z)%ab
# print(chinese,"is the required value")

#FERMAT'S LITTLE THEORM
# import numpy as np
# a=int(input("Enter the number : "))
# p=int(input("Enter the power of the number : "))
# m=int(input("Enter the mod value : "))
# import numpy as np
# f=np.gcd(a,m)
# print(f)
# if(f==1):
#     print("Exists....")
# else:
#     print("Does not exists...")
# b=m-1
# e=p%b
# print((a.__pow__(e))%m,"is the final remainder value by fermats little theorm")
# def twosum(*arr,target):
#     for i in range(arr):
#         for j in range(arr):
#             if(i+j==target):
#                 print(i,j)
# arr=[2,7,11,15]
# target=9
# result=twosum(*arr,target)
# print(result)
# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return [num_map[complement], i]
#         num_map[num] = i
#     return []
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum(nums, target)
# print(result) 

#TIC-TAC-TOE
i=1
from random import randint
board=["_","_","_","_","_","_" ,"_","_","_"]
def boards():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
def position():
    p=int(input("Enter the position : "))
    while p not in [0,1,2,3,4,5,6,7,8]:
        print("Enter the valid position from 0-8 ")
        p=int(input("Enter the new position : "))
    if (board[p]!="_"):
            print("The position is already taken .Enter the new position")
            p=int(input("Enter the position : "))
            board[p]="O"
            boards()
            
    else:
        board[p]="O"
        boards()
        
def computer():
    y=randint(0,8)
    print("The computer has selected position : ",y)
    if (board[y]!="_"):
         print("The computer is taking another position pls wait....")
         computer()
         boards()
    else:
        board[y]="X"
        boards()
def available_positions():
    print("The vaialable positions are : ")
      
while(i<=8):
     position()
     if((board[0]==board[3]==board[6]!="_" or board[1]==board[4]==board[7]!="_" or board[2]==board[5]==board[8]!="_" or board[0]==board[4]==board[8]!="_" or board[2]==board[4]==board[6]!="_" or board[0]==board[1]==board[2]!="_" or board[3]==board[4]==board[5]!="_" or board[6]==board[7]==board[8]!="_") == "X"):
      print("Computer won the game")
      print("Game is over")
      break
     if(board[0]==board[3]==board[6]!="_" or board[1]==board[4]==board[7]!="_" or board[2]==board[5]==board[8]!="_" or board[0]==board[4]==board[8]!="_" or board[2]==board[4]==board[6]!="_" or board[0]==board[1]==board[2]!="_" or board[3]==board[4]==board[5]!="_" or board[6]==board[7]==board[8]!="_" == "O"):
      print("You won the game","Congratulations")
      print("Game is over")
      break
     computer()
     print("the available postions ",end=" ")
     for i in range(0,8):
         if board[i]=="_":
             print(i,end=" ")
             
     else:
      i=i+1

    
            


