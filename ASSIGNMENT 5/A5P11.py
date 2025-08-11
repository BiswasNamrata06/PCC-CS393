def sum_positive(args):
    return sum(x for x in args if x > 0)

num = int(input("Enter the number of arguments: "))
args = []
for i in range(num):
    x = float(input(f"Enter argument {i+1}: "))
    args.append(x)
result = sum_positive(args)
print("Sum of positive numbers:", result)
