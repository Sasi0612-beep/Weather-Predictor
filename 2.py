# #MODULO INVERSE

# def modinv(a,b):
#    if(a>0):
#     print(a%b)
#    else:
#      q=a//b
#      r=q*b
#      m=abs(r)+a
#      print(m)
# modinv(39,4)
# modinv(-39,4)
# modinv(-128,4)

# # INVERSE TABLE

# #ADDITION
# a=int(input("Enter the number : "))
# print("This is for addition")
# for i in range(0,a):
#      print(end="\n")
#      for j in range(0,a):
#       print((i+j)%a,end=" ")
# print(end="\n")

# #MULTIPLICATION

# a=int(input("Enter the number : "))
# print("This is for multiplication")
# for i in range(0,a):
#      print(end="\n")
#      for j in range(0,a):
#       print((i*j)%a,end=" ")

# a=int(input("Enter the number : "))
# p=int(input("Enter the power of the number : "))
# m=int(input("Enter the m value : "))
# print((a**p)%m)
# import cowsay
# cowsay.cow("Hello world")
# print(cowsay.get_output_string("cow","helloworld"))
# cowsay.cow('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris blandit rhoncus nibh. Mauris mi mauris, molestie vel metus sit amet, aliquam vulputate nibh.')
# print(cowsay.get_output_string("milk","helloworld"))
# cowsay.cow("sharks are my bestfriends")
# cowsay.trex("hi sasi")
# def squares():
#     x=int(input("Enter the number : "))
#     print("The square of the number is : ",square(x))
#     assert square(0)==0
#     assert square(7)==49
#     assert(square(3))==9
# def square(x):
#     return x+x
# squares()
# import csv

# students=[]
# with open("names.txt") as file:
#   reader=csv.DictReader(file)
#   for row in reader:
#      students.append({"name":row["name"],"home":row["home"],"house":row['house']})
# for student in sorted(students,key=lambda student:student['name']):
#     print(f"{student['name']} is from {student['home']} and is in {student['house']}")
# import csv
# name=input("Whats your name ?")
# home=input("Whats your home ? ")
# with open("names.txt","a") as file:
#     writer=csv.DictWriter(file,fieldnames=["name","home"])
#     writer.writerow({"home":home,"name":name,})
a=int(input("Enter the number : "))
d={1:"Monday",2:"Tuesday"}
if a in d.keys():
    print(a,"is",d[a])