from itertools import permutations,combinations
num = int(input("Enter the number of elements in the list: "))
elements = [input(f"Enter element {i+1}: ") for i in range(num)]
print("Permutations:")
for p in permutations(elements):
    print(p)
print("Combinations:")
for r in range(1,num+1):
    for c in combinations(elements,r):
        print(c)