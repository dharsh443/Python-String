S=input("Enter the string:")

count=0
for cha in S:
    if(ord(cha)%2==0):
        count=count+1

print(count)
