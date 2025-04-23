
# number=8247358258
# temp=number
# dig=8
# length=0
# place=[]
# count=0
# sree=False
# while number>0:
    
#     number=number//10 #824735825
#     length+=1#1---#10
# while temp>0:
#     last=temp%10 #8 2 4 7 3 5 8 2 5 8 
#     if last==dig: 
#         sree=True
#         place.append(length)
#         count+=1
#     length-=1
#     temp=temp//10
# if sree:
#     print(place)
#     print(count)
# else:
#     print("doesn't exist")

num=87654320
temp=num
prev=num%10  #1 2 3 4 5 6 7 8 
is_descending=True 
while num>0:
    last_digit=num%10 #1 2 3 4 5 6 7 8
    if last_digit<prev:
        is_descending=False
        break
    prev = last_digit
    num=num//10
if is_descending:
    print(temp, "is in descending order")
else:
    print(temp,"is not in descending order")

