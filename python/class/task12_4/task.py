# task1
list=[1,2,4,5,19,15,12,9,7]
small=min(list)
big=max(list)
missing=[]
for i in range(small,big+1):
    if i not in list:
        missing.append(i)
print(missing)


#Take a dictionary with salaries and Find percentage of the salaries
salaries={
    "udayasree":40000,
    "nani":35000,
    "maheshbabu":45000,
    "viratkohli":60000,
    "dhoni":50000
}
total=0
for i in salaries:
    total=total+salaries[i]
for key in salaries:
    
    percentage=(salaries[key])/total*100
    print(key,percentage)



