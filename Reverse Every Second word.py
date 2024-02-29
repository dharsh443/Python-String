S=input("Enter the string:")
L=S.split()
i=0
L1=[]
while(i<len(L)):
    if(i%2 == 0):
        L1.append(L[i])
    else:
        L1.append(L[i][::-1])
    i=i+1
B=' '.join(L1)
print(B)
