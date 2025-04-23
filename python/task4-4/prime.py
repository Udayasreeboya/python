num=int(input("enter the number: "))
prime_not_found=True
while prime_not_found:
    num-=1
    fact=0
    for i in range(2,num):
        if num%i==0:
            fact+=1
            break
    if fact==0:
        print(f"previous prime number is{num}")

        prime_not_found=False
