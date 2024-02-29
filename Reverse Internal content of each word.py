S=input("Enter the string:")
A=S.split()
print(A)
L=[]
for word in A:
    L.append(word[::-1])
C=' '.join(L)
print(C)
