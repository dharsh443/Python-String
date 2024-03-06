String1=input("Enter the String 1:")
String2 =input("Enter the String 2:")
if(len(String1)==len(String2)):
    if(sorted(String1)== sorted(String2)):
        print("The entered String is ANAGRAM")
    else:

        print("Not a ANAGRAM")
      
else:
    print("Not a ANAGRAM")
    
