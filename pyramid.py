#Print the pyramid of numbers using for loops.

n=int(input("enter the number of rows"))
for i in range(0,n):
    for j in range (0,n-i-1):
        print(' ',end='')
    for k in range(0,i+1):
        print('*',end=' ')
    print()