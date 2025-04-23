# name="udayasree"
# count=0
# for i in name:
#     count+=1
#     if count==5:
#         new=name.replace(i,"k")
# print(new)


a=0
b=1
count=0
while a<500:
    print(a, end=",")
    count+=1
    c=a+b
    a=b
    b=c
print("\n there are: ",count , "number of Fibonacci numbers")

