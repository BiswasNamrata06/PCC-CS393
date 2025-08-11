num=int(input("Enter the number of elements in the list:"))
elements=[input(f"Enter the element {i+1} : ") for i in range(num)]
unique=[]
for i in elements:
    if not i in unique:
        unique.append(i)
print(unique)