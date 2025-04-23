# my_tuple=(1,2,3,4,5,6,1,2,3,4,5,6,8,4)
# num=4
# occ=3
# count=0
# if my_tuple.count(num)>=occ:
#     for i in range(0,len(my_tuple)):
#         if my_tuple[i]==num:
#             count+=1
#         if count==3:
#             print(i)
#             break

# else:
#     print("it is not in list")

my_tup=(1,2,3,4,5,4,5,6,8,9,2,4)
uniq=[]
count=0
for i in range(0,len(my_tup)):
    count=my_tup.count(my_tup[i])
    if count==1:
        uniq.append(my_tup[i])
print(uniq)
