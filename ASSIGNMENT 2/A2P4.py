q=int(input("Enter how many numbers you want to input:"))
numbers=[]
reverse=[]
for i in range(q):
    num=input(f"Enter the {i+1} number:")
    numbers.append(num)
    reverse.append(num[::-1])
for i in range(q):
    if reverse[i]==numbers[i]:
        print(f"The number {numbers[i]} is a palindrome number ")
