word=input("Enter the word:")
word=list(word)
i=0
while i<len(word)-1:
    if word[i]==word[i+1]:
        del word[i:i+2]
        i=0
    else:
        i+=1
if word:
    for i in word:
        print(i,end="")
else:
    print("Empty string")
        
