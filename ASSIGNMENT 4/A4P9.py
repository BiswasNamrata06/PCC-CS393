def search(elements, key,num):
    for i in range(num):
        if elements[i] == key:
            return i  
    return -1  

num=int(input("Enter the number of elements in the list:"))
elements=[int(input(f"Enter the element {i+1} in the list")) for i in range(num)]
key=int(input("Enter the element to be searched:"))
if search(elements,key,num)!=-1:
    print(f"Element found at index {search(elements,key,num)}")
else:
    print("Element not found")