def multi_table(n , m):
    for i in range(1 , n+1):
        for j in range(1,m+1):
            print('{:>4}'.format(i*j),end='')
            if j == m :
                print()

n = int(input("enter your number1:"))
m= int(input("enter yore number2:"))

multi_table(n , m)