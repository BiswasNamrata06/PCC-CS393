num = int(input("Enter the number of elements in the lists: "))

M = [int(input(f"Enter element {i+1} of list M: ")) for i in range(num)]
L = [int(input(f"Enter element {i+1} of list L: ")) for i in range(num)]

N = [m + l for m, l in zip(M, L)]

print("List M:", M)
print("List L:", L)
print("List N :", N)

    
    