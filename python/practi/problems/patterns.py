n=7
for i in range(1,n+1,1):
    print(" " * (n - i) + "*" *  i )
n=10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
num=18
fact=0
for i in range(1,num+1):
    if num%i==0:
        fact+=1
if fact==2:
    print(num, "is prime number")
else:
    print(num, "is  not prime number")
low=int(input("enter the start value: "))
prime=[]
product=1
for i in range(1,low+1,1):
    fact=0
    for j in range(1,i+1,1):
        if i%j==0:
            fact+=1
    if fact==2:
        product*=i
print(product)
        


num=6
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


num=121
temp=num
reverse=0
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
    print(temp)
if num==reverse:
    print("polindrome")
else:
    print("not polindrome")



name="malayalam"
reverse=""
for i in range(len(name)-1,-1,-1):
    reverse+=name[i]
print(reverse)
if name==reverse:
    print("polindrome")
else:
    print("not polindrome")
s1="listen"
s2="silent"
ana=True

if len(s1)!=len(s2):
    ana=False
else:
    for i in range(len(s1)):
        if s1.count(s1[i])!=s2.count(s1[i]):
        ana=False
        break
if ana:
    print("anagram")
else:
    print("not anagram")

s1="silent"
s2="listen"
ana=True
for i in range(len(s1)):
    if s1.count(s1[i])!=s2.count(s2[i]):
        ana=False
        break
if ana:
    print("anagram")
else:
    print("not anagram")


s1="silent"
s2="listens"
ana=True
for i in range(1,len(s1)):
    if s1.count(s1[i])!=s2.count(s2[i]):
        ana=False
        break
if ana:
    print("anagram")
else:
   print("not anagrams")

num=123212
temp=num
reverse=0
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
print(reverse)
string="madam"
reverse=""
for i in range(len(string)-1,-1,-1):
   reverse+=string[i]
print(reverse)
if string==reverse:
   print("polindrome")
else:
    print("not polindrome")

n=10
n1=1
n2=2
print(n1,n2,end=",")
for i in range(n1,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=",")
    print()


num1=18
num2=16
for i in range(max(num1,num2),(num1*num2)+1):
    if i%num1==i%num2==0:
       lcm=i
print(lcm)

num1=19
num2=38
for i in range(1,min(num1,num2)+1):
  if num1%i==num2%i==0:
    hcf=i
print(hcf)

# print(chr(62))
num=[1,2,3,4]
num.insert(7,2)
print(num)