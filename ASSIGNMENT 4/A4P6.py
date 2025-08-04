num=int(input("Enter the number of elements in the list:"))
elements=[input(f"Enter the element {i+1} in the list") for i in range(num)]
temp=set()
unique=[]
duplicates=[]
for i in elements:
    if i not in temp:
        temp.add(i)
        unique.append(i)
    else:
        duplicates.append(i)
final=unique+ duplicates
print(f"The output is:{final}")
    