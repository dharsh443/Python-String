S=input("Enter the string:")
pre=S[0]
c=1 #count
i=1 #index
output=''
while (i<len(S)):
    if(S[i]==pre):
        c=c+1
    else:
        output=output+pre+str(c)
        pre=S[i]
        c=1
    if(i== len(S)-1):
        output=output+pre+str(c)
    i=i+1
print(output)
        
        
