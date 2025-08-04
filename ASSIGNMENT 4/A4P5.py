num=int(input("Enter the number of elements in the list:"))
numbers=[input(f"Enter the element {i+1} in the list:") for i in range (num)]

start=int(input("Enter the start index:"))
end=int(input("Enter the end index:"))
if start<0 or end>=len(numbers)or start>end:
    print("Invalid input")
else:
    index_list=numbers[start:end+1]
    print(f"The list of numbers in the range is {index_list}")
    print(f"The maximum number in the index is :{max(index_list)}")
    print(f"The minimum number in the range is {min(index_list)}")
