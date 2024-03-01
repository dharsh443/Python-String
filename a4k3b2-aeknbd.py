s=input("Enter the string:")
output=''
for ch in s:
    if(ch.isalpha()):
        output+=ch
        x=ch
    else:
        d=int(ch)
        new=chr(ord(x)+d)
        output+=new
print(output)
