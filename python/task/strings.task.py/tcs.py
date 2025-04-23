n1=int(input("enter the number: "))
n2=int(input("enter the number2: "))
maximum=max(n1,n2)
prime_count=0
prime_num=2
while prime_count<maximum:
    fact=0
    for i in range(2,prime_num):
        if prime_num%i==0:
            fact+=1
            break
    if fact==0:
            prime_count+=1
            if prime_count==n1 or prime_count==n2:
                print(prime_num)
    prime_num+=1
# print(prime_num)
