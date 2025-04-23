
num=50
for i in range(num,1,-1):
    fact=0
    for j  in range(2,i):
        if i%j==0:
            fact+=1
            break
    if fact==0:
        print(i)
        break