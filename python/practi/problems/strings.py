# a="""udayasree is a 'software' developer"""
# print(a[len(a)-1])
# print(a[9])
#methods for strings
# 1.upper()--
# name="udayasree57"
# print(name.upper())
# 2. lower()
# name="     Udaya   SREE  "
# print(name.lower())
# 3. strip--it removes the spaces on both sides starting and ending
# print(name.strip())
# 3.1.lstrip--it removes spaces on left side only
# print(name.lstrip())
# 3.2.rstrip--it removes spaces on right side only
# print(name.rstrip())


#4. replace
# name="my name is udayasree, i am final year student"
# print(name.replace("e","E"))
# print(name.replace("udayasree","nanii"))


# #startswith--
# name="Udayasree"
# print(name.startswith("u"))
# #endswith
# print(name.endswith("e"))


#find--
# name="udayasree is learning python is intersesting"
# print(len(name),  name.find("t"))

#count---
# name="udayasree"
# print(name.count("a"))

#title--
# sentence="ramudu is good boy"
# print(sentence.title())

#capitalize---
# name="my name is udayasree. i am from anantapur"
# print(name.title())
# print(name.capitalize())

name="udayasree"
vowels="aeiou"
for i in range(0,len(name),1):
    ch=name[i]
    if vowels.find(ch)!=-1:
        print(ch)
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" :
        print(ch)
for i in name:
    if i not in vowels:
        print(i)

