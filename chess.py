def chess(n , m):
    
    for i in range(1 ,n+1):
        
        
        for j in range(1 , m+1):
            
            
            if (i+j) % 2 == 0:
              print('{:>4}'.format(' # '),end=' ' )
            else :
              print('{:>4}'.format(' * '), end='')  
        print()       

n= int(input("enter number for row:"))
m= int(input("enter number for column:"))


chess(n , m)

