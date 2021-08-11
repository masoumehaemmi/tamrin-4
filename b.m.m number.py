import math

a= int(input("enter your number 1:"))
b= int(input("enter your number 2:" ))

for i in range(a):
    if a>b :
        a = a-b
    elif a<b:
        t= a
        a= b
        b=t
    elif a == 0:
        print()

print ("b.m.m :" , b)        
