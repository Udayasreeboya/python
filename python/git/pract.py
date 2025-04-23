list=[1,2,3,4,5,5,6,9,13,11,17,19]
prime=[]
non_prime=[]
for i in range(0,len(list)):
    fact=0
    for j in range(1,list[i]+1):
        if list[i]%j==0:
            fact+=1
    if fact==2:
        prime.append(list[i])
    else:
        non_prime.append(list[i])

print((prime))
print(non_prime)

list=[1,2,3,4,5,6,7,11,13,-1]
prod=1
for i in range(0,len(list),1):
    fact=0
    for j in range(1,list[i]+1,1):
        if list[i]%j==0:
            fact+=1
    if fact==2:
        prod=prod*list[i]
print(prod)
l=[1,2,3,4,5,6,1]
m=min(l)
for i in range(len(l)):
    print(m-l[i])

list=[]
value=10
for x in range(1,value+1):
    inp=int(input("enter the element:"))
    list.append(inp)
    prod=1
for i in range(0,len(list),1):
    fact=0
    for j in range(1,list[i]+1,1):
        if list[i]%j==0:
            fact+=1
    if fact==2:
        prod=prod*list[i]
print(prod)



         
