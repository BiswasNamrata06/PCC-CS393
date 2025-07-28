def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
if num<0:
    print("Factorial for negative numbers is not defined")
else:
    print(f"Factorial for {num} is {factorial(num)}")