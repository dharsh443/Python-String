print("Enter the input of same LENGTH:")
A=input("Enter the String1:")
B=input("Enter the String2:")
i,j=0,0
output=''
while(i<len(A) or j<len(B)):
    output+=A[i]+B[i]
    i+=1
    j+=1
print(output)
