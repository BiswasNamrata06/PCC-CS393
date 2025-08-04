num=int(input("Enter the number of elements in the list:"))
list1=[input(f"Enter the element {i+1} in the list 1:") for i in range(num)]
list2=[input(f"Enter the element {i+1} in the list 2:") for i in range(num)]
for i in range(num):
    if list1[i]!= list2[i]:
        print(f"The index where they start to differ is {i}")
        break
else:
        print("The two lists are identical")