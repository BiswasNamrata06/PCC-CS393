string=input("Enter the string:")
string=list(string)
upper=0
lower=0
for i in string:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(f"The number of uppercase character is {upper} and the number of lowercase character is {lower}")