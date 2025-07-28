import string
def caesar_cipher(key,word,EorD):
    if key<0:
        print("Invalid Input")
        return
    letters=list(string.ascii_lowercase)
    output=[]
    
    for ch in word:
        if ch in letters:
            index=letters.index(ch)
            if EorD=="E":
                new_key=(index+key)%26
            elif EorD=="D":
                new_key=(index-key)%26
            else:
                print("Invalid choice")
                return
            new_char=letters[new_key]
            output.append(new_char)
        elif ch.isdigit():
            digit=int(ch)
            if EorD=="E":
                new_digit=(digit+key)%10
            elif EorD=="D":
                new_digit=(digit-key)%10
            else:
                print("Invalid Input")
                return
            output.append(str(new_digit))
        else:
            output.append(ch)
    print("The output is :")   
    for ch in output:
        
        print(ch,end="")
        
text=input("Enter the text you want to encode or decode:")
text=text.lower()
key=int(input("Enter the value of the key:"))
E_d=input("Enter \"E\" if you want to Encode and enter \"D\" if you want to Decode")
E_d=E_d.upper()
caesar_cipher(key,text,E_d)
            
        
    