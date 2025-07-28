import string
def is_pangram(sentence):
    letters=list(string.ascii_lowercase)
    sentence=sentence.lower()
    
    for i in letters:
        if i not in sentence:
            return False
    else:
        return True
    
text = input("Enter a sentence: ")
if is_pangram(text):
    print("It is a pangram.")
else:
    print("It is not a pangram.")

    