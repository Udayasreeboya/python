list=[1,3,5,10,16,20,100,55,25,20,65,88]
out=filter(lambda ele:ele%5==0,list)
out=tuple(out)
print(out)



#using map
list=[1,3,5,10,16,20,100,55,25,20,65,88]
out=map(lambda ele:ele%5==0,list)
out=tuple(out)
print(out)

string="udayasree"
vowels="aeiou"
out=filter(lambda char:char in vowels,string)
out=tuple(out)
print(out)

#using map
string="udayasree"
vowels="aeiou"
out=map(lambda char:char in vowels,string)
out=tuple(out)
print(out)



