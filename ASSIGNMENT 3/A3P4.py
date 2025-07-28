word=input("Enter the string:")
word=word.lower()
reverse=word[::-1]
if word==reverse:
    print("It is an palindrome")
else:
    print("It is not an palindrome")