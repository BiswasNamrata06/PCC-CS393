num=[]
denum=[]
fractions=[]
n=int(input("Enter the number of fraction:"))
for i in range(n):
    frac=input(f"Enter the fraction {i+1}:")
    parts=frac.split('/')
    numerator=int(parts[0])
    denominator=int(parts[1])
    if denominator==0:
        print("Denominator cannot be zero")
        exit()
    num.append(numerator)
    denum.append(denominator)
    fractions.append(numerator/denominator)
min_value=min(fractions)
max_value=max(fractions)
min_index=fractions.index(min_value)
max_index=fractions.index(max_value)
print(f"Smallest fraction is {num[min_index]}/{denum[min_index]} and its index is{min_index}")
print(f"Largest fraction is {num[max_index]}/{denum[max_index]} and its index is{max_index}")

    
