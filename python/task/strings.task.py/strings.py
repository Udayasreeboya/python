para="""my name is udayasree, I'm from anantapur
 district. currently im persuing btech final 
 year at mohan babu university, tirupati"""
if len(list(para))>100:
    print("valid paragraph")
else:
    print("not valid paragraph")


# task2: to print the count of uppercases and lower cases words
string=input("enter the string with upper and lower words: ")
uppercase=0
lowercase=0
for i in string:
    if ord(i)>=65 and ord(i)<=92:
        uppercase+=1
    elif ord(i)>=97 and ord(i)<=122:
        lowercase+=1
print("lowercase characters are", lowercase)
print("uppercase characters are",uppercase)