S=input("Enter the string:")
output=''
for ch in S:
    if(ch.isalpha()):
        X=ch
    else:
        Y=int(ch)
        output+=X*Y
print(output)
