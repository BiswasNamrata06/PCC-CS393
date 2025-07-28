row=(int(input("Enter the number of rows:")))

for j in range (row,0,-1):
    star=2*j-1
    space=row-j
    print(" "*space + "*"*star)        