String=input("Enter the String:")
Half=int(len(String)/2)
first=String[:Half]
second=String[Half:]

if(first==second):
    print("Symmetrical")
else:
    print("Not Symmetrical")
if(first==second[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")
