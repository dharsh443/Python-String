S=input("Enter the String:")
output=''
i =len(S)-1
for ch in  S:
    output=output+S[i]
    i=i-1
print(output)
