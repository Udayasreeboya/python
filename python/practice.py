"""
num=15
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")

year=2019
if (year%400==0) or (year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not leap year")
"""
# num=1234321
temp=num
reverse=0
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
if reverse==num:
    print("polindrome number")
else:
    print("not polindrome number")

