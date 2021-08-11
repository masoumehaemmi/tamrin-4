import math
a= int(input("enter your number 1:"))
b= int(input("enter your number 2:"))

for i in range(a):
   if a>b:
       c = a % b
       bm=b/c  
       print(bm)
   elif c == 0:   
       d=a*b
       km=d/c
       print(km)
print("k.m.m :" ,km)
