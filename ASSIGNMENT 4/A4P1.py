import string
letters = list(string.ascii_lowercase)
output = []

for i in range(26):
    output.append(letters[i] * (i + 1))

print(output)
