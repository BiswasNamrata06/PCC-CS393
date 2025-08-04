num=int(input("Enter the number of elements in the list:"))
elements=[input(f"Enter the element {i+1} in the list") for i in range(num)]
start=0
end=num-1
while start<end:
    temp=elements[start]
    elements[start]=elements[end]
    elements[end]=temp
    start+=1
    end-=1
print(",".join(elements))