def integers(start):
    return [start+i for i in range(10)]
start=int(input("Enter the starting integer:"))
print(f"The list of integers is {integers(start)}")