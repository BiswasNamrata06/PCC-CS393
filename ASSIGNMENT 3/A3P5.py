import string
def superascii(word):
    letters=list(string.ascii_lowercase)
    freq={}
    for ch in word:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
            
    print(freq)
    for ch in freq:
        if freq[ch]!=letters.index(ch)+1:
            return False
    return True
text=input("Enter the string:")
if superascii(text):
    print("It is a Super ASCII")
else:
    print("Its is not a Super ASCII")
    
            
        