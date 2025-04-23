# num1=int(input("enter the 1st number: "))
# num2=int(input("enter the 2nd number: "))
# num3=int(input("enter the 3rd number: "))
# big=max(num1,num2,num3)
# if big%num1==0 and big%num2==0 and big%num3==0:
#     print(f"{big} is the lcm")
# else:
#     temp=big
#     while True:
#         if temp%num1==0 and temp%num2==0 and temp%num3==0:
#             print(f"{temp} is the lcm")
#             break
#         temp+=big

#palindrome on string
palindrome="malayalam"
reverse=""
for i in range(len(palindrome)-1,-1,-1):
    reverse+=palindrome[i]
if reverse==palindrome:
    print(f"{palindrome} is palindrome")
else:
    print(f"{palindrome} is not palindrome")

#palindrome on numbers
num=1221
temp=num
reverse=0
while num>0:
    remainder=num%10
    reverse=reverse*10+remainder
    num=num//10
if reverse==temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")
