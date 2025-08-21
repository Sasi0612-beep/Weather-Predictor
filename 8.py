import numpy as np
a=np.array([[1,2],
            [4,5]])
b=np.array([[7,8],
             [13,14]])
print("multiplication of two matrices is : \n",a.dot(b))
print("addition of two matrices is : \n",a+b)
print("lcm of two matrcises is ")
a=np.array([0,np.pi/2,np.pi])
print(np.sin(a))
print(np.exp(a))

x="hello"
for i in x: 
    print(i)
array=np.arange(8)
print(array)
print(array.reshape(2,4))
print(array.reshape(4,2))

print(np.linspace(2.0,3.0,num=5,retstep=True),"\n")

list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
a1=np.array(list1)
a2=np.array(list2)
print("multiplication of two matrices gives : ",a1*a2)
a=np.array([[1,2,3],
            [4,5,6],
            [8,9,1]])
print("rank of the matrix is : ",np.linalg.matrix_rank(a))
print(np.trace(a),"is the trace of the matrix")
print(np.linalg.det(a),"is the determinant of te matrix")
print(np.linalg.inv(a),"is the inverse of the matrix")

a=np.diag((1,2,3))
print(np.linalg.eig(a))
print("eigen values of the matrix is : ")

def foo():
    print(5)
def goo():
    return 7
foo()
y=goo()
print(y)

def fac(n):
    if n==1:
        return n
    else:
        return (n)*fac(n-1)
no=int(input("enter the number : "))
if(no<0):
    print("factorial does not exist")
else:
    print("the factorial of n is : ",fac(no))

def fib(n):
    if n==1: 
        return n
    else:
        return (n-1)+fib(n-2)
no=10
if no<=0:
    print("enter the correct number")
else:
    print("the fibanocci series are : ",fib(no))

