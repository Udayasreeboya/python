num=[1,2,3,4,5,6,7,8,9,10,0,11,51,67,84]
prime=[]
non_prime=[]
for i in range(0,len(num)):
    fact=0
    for j in range(1,num[i]+1):
        if num[i]%j==0:
            fact+=1
    if fact==2:
        prime.append(num[i])
    else:
        non_prime.append(num[i])
print(prime)
print(non_prime)

# def check_prime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num%i == 0:
#             count+=1
#     if count == 2:
#         return True