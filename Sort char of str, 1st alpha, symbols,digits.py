String=input("Enter the string:")
Alphabet=[]
Digit=[]
for ch in String:
    if(ch.isalpha()):
        Alphabet.append(ch)
    else:
        Digit.append(ch)
output=''.join(sorted(Alphabet)+sorted(Digit))
print(output)
