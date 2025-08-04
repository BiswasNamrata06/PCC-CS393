import math
num=int(input("Enter the number of elements in the list:"))
elements=[int(input(f"Enter the element {i+1} in the list")) for i in range(num)]
mean=sum(elements)/num
varience= sum((i-mean)**2 for i in elements)/num
std=math.sqrt(varience)
print(f"Mean:{mean:.2f}")
print(f"Varience:{varience:.2f}")
print(f"Standard deviation:{std:.2f}")

    