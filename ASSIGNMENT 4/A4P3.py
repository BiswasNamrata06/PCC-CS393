num=int(input("Enter the number of strings in the list:"))
if num<=0:
    print("List should have at least 1 element")
    exit()
str_list=[input(f"Enter the string {i+1} :") for i in range(num)]
max_length = max(len(s) for s in str_list)
longest_string = [s for s in str_list if len(s) == max_length]
print(f"The longest string is {",".join(longest_string)} and its length is {max_length}")

