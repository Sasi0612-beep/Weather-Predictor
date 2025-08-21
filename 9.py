# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# list3=[x+y for x,y in zip(list1,list2)]
# list4=[x-y for x,y in zip(list1,list2)]
# list5=[x*y for x,y in zip(list1,list2)]
# list6=[x/y for x,y in zip(list1,list2)]
# print("addition is : ",list3)
# print("subtraction is : ",list4)
# print("multiplication is : ",list5)
# print("division is : ",list6)

# import numpy as np
# import math
# x=[np.pi/2,np.pi/4,np.pi/6,np.pi/3]
# y=np.sin(x)
# a=np.cos(x)
# b=np.tan(x)
# print(y,"are the values of sin")
# print(a,"are the values of cos")
# print(b,"are the values of tan")

# import numpy as np
# arr=np.array([[1,2,3],
#             [4,5,6],
#             [7,8,3]])
# brr=np.array([[3,2,1],
#                 [6,5,4],
#                 [9,8,7]])
# print(arr)
# print(brr)
# print(arr+brr)
# print(arr-brr)
# print(arr.dot(brr))
# print(arr/brr)
# print(arr.T)
# print(brr.T)
# print(arr.max())
# print(brr.max())
# print(arr.max(axis=0))
# print(arr.max(axis=1))
# print(np.exp(arr))
# print(np.sqrt(arr))
# print(arr.size)
# print(arr.shape)
# print(arr.flatten())
# print(np.linalg.det(arr))
# print(np.trace(arr))
# print(np.linalg.matrix_rank(arr))
# print(np.linalg.inv(arr))

# #logarithams and exponents
# import numpy as np
# list1=[2,3,4,5,6,7]
# arr=np.array(list1)
# print(np.log2(arr))
# print(np.log10(arr))
# print(np.log(arr))
# from math import log
# import numpy as np
# nplog=np.frompyfunc(log,2,1)
# print(nplog(100,3))
# print(np.exp(arr))
# print(nplog(100,3),nplog(100,4),nplog(100,5))

# #inverse trigonometric functions
# import numpy as np
# arr=np.array([1.0,-1,0.5,0.8])
# print(np.arcsin(arr))
# print(np.arccos(arr))
# print(np.arctan(arr))
# print(np.arcsinh(arr))
# print(np.arccosh(arr))
# print(np.arctanh(arr))
# def check_closure(seq):
#     checked = set(set())
#     m = len(seq)
#     for i in range(len(seq)):
#         for j in range(len(seq)):
#             if (seq[i] + seq[j]) % m in seq:
#                 checked.add((seq[i], seq[j]))
#             else:
#                 return False
#     return True, checked
 
 
# def check_associativity(seq):
#     checked = set(set())
#     m = len(seq)
#     for i in range(len(seq)):
#         for j in range(len(seq)):
#             for k in range(len(seq)):
#                 if (seq[i] + (seq[j] + seq[k])) % m == (
#                     (seq[i] + seq[j]) + seq[k]
#                 ) % m:
#                     checked.add((seq[i], seq[j], seq[k]))
#                 else:
#                     return False
#     return True
 
 
# def check_identity(seq):
#     m = len(seq)
#     valid = []
#     for i in range(len(seq)):
#         temp = []
#         for j in range(len(seq)):
#             if (seq[i] + seq[j]) % m == seq[j]:
#                 print(f"{seq[i]} + {seq[j]} mod {m} = {(seq[i] + seq[j]) % m}")
#                 temp.append(seq[j])
#             else:
#                 break
#         valid.append(temp)
 
#     for i in range(len(valid)):
#         if len(valid[i]) == m:
#             return True, seq[i]
#     return False
 
 
# def check_inverse(seq):
#     m = len(seq)
#     if identity := check_identity(seq):
#         identity = identity[1]
#     else:
#         return False
#     inverses = []
#     for i in range(len(seq)):
#         for j in range(len(seq)):
#             if (seq[i] + seq[j]) % m == identity:
#                 inverses.append(seq[j])
#                 break
 
#     if len(inverses) == m:
#         return True, {i: j for i, j in zip(seq, inverses)}
#     return False
 
 
# def check_commutativity(
#     seq,
# ) :
#     valid = set(set())
#     m = len(seq)
#     for i in range(len(seq)):
#         for j in range(len(seq)):
#             if i <= j:
#                 if (seq[i] + seq[j]) % m == (seq[j] + seq[i]) % m:
#                     valid.add((seq[i], seq[j], seq[j], seq[i]))
#                 else:
#                     return False
#     return True, valid
 
# seq = [i for i in range(5)]
 
# print("Checking closure: ")
# print(check_closure(seq))
# print("\nChecking associativity: ")
# print(check_associativity(seq))
# print("\nChecking identity: ")
# print(check_identity(seq))
# print("\nChecking inverse: ")
# print(check_inverse(seq))
# print("\nChecking commutativity: ")
# print(check_commutativity(seq))

# if(check_closure(seq),check_associativity(seq),check_identity(seq),check_inverse(seq),check_commutativity(seq)):
#      print("The given sequence is an abelian group")
# else:
#      print("The given sequence is not an abelian group")
from graphviz import Digraph

# Create a new directed graph
er_diagram = Digraph("eCommerce_Shipping_Prediction_ER", node_attr={'shape': 'record', 'height': '.1'})

# Adding Customer entity
er_diagram.node('Customer', '''{Customer | 
                              CustomerID (PK) | 
                              Name | 
                              Email | 
                              PhoneNumber | 
                              ShippingAddressID (FK) | 
                              OrderID (FK)}''')

# Adding Order entity
er_diagram.node('Order', '''{Order | 
                            OrderID (PK) | 
                            OrderDate | 
                            CustomerID (FK) | 
                            TotalAmount | 
                            ShippingCostID (FK) | 
                            ShippingPredictionID (FK)}''')

# Adding Product entity
er_diagram.node('Product', '''{Product | 
                              ProductID (PK) | 
                              ProductName | 
                              Weight | 
                              Dimensions | 
                              Price | 
                              Category}''')

# Adding Shipping Address entity
er_diagram.node('ShippingAddress', '''{Shipping Address | 
                                      ShippingAddressID (PK) | 
                                      Street | 
                                      City | 
                                      State | 
                                      Country | 
                                      ZipCode}''')

# Adding Warehouse entity
er_diagram.node('Warehouse', '''{Warehouse | 
                                WarehouseID (PK) | 
                                Location | 
                                Capacity}''')

# Adding Shipping Carrier entity
er_diagram.node('ShippingCarrier', '''{Shipping Carrier | 
                                      CarrierID (PK) | 
                                      Name | 
                                      ServiceType | 
                                      TrackingURL}''')

# Adding Shipping Prediction entity
er_diagram.node('ShippingPrediction', '''{Shipping Prediction | 
                                         PredictionID (PK) | 
                                         EstimatedDeliveryTime | 
                                         CarrierID (FK) | 
                                         AlgorithmID (FK)}''')

# Adding Shipping Cost entity
er_diagram.node('ShippingCost', '''{Shipping Cost | 
                                   ShippingCostID (PK) | 
                                   Cost | 
                                   CarrierID (FK) | 
                                   Weight}''')

# Adding Shipping Status entity
er_diagram.node('ShippingStatus', '''{Shipping Status | 
                                     StatusID (PK) | 
                                     OrderID (FK) | 
                                     Status | 
                                     Timestamp}''')

# Adding Prediction Algorithm entity
er_diagram.node('PredictionAlgorithm', '''{Prediction Algorithm | 
                                          AlgorithmID (PK) | 
                                          AlgorithmName | 
                                          ModelVersion}''')

# Adding External Data entity
er_diagram.node('ExternalData', '''{External Data | 
                                   DataID (PK) | 
                                   DataType | 
                                   DataSource | 
                                   Timestamp}''')

# Defining relationships
er_diagram.edge('Customer', 'Order', label='Places')
er_diagram.edge('Order', 'Product', label='Contains')
er_diagram.edge('Customer', 'ShippingAddress', label='Uses')
er_diagram.edge('Order', 'ShippingPrediction', label='Has')
er_diagram.edge('ShippingPrediction', 'ShippingCarrier', label='Uses')
er_diagram.edge('Order', 'ShippingCost', label='Has')
er_diagram.edge('ShippingCost', 'ShippingCarrier', label='Set By')
er_diagram.edge('ShippingPrediction', 'PredictionAlgorithm', label='Predicted By')
er_diagram.edge('ShippingPrediction', 'ExternalData', label='Uses')
er_diagram.edge('Order', 'ShippingStatus', label='Updates')
er_diagram.edge('ShippingStatus', 'Order', label='Tracks')
er_diagram.edge('Product', 'Warehouse', label='Stored In')

# Render the ER diagram
er_diagram
