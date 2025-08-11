num=int(input("Enter the total number of elements:"))
elements=[int(input(f"Enter the {i+1} element in the list:")) for i in range(num)]
elements.sort()
if num%2==0:
    median=(elements[num//2]+elements[(num//2)-1])/2
else:
    median=elements[num//2]
print(f"The median is {median}")