"""
#default parameters
def friends_info(name,batch_name="66b",place="beluguppa"):
    print(name+batch_name+place)
friends_info("udayasree")
friends_info("krishna")
friends_info("devika")
friends_info("raj")


#keyword arguments
def user_info(f_name,l_name):
    print(f_name+" "+l_name)
user_info(l_name="boya",f_name="udayasree")

#positional arguments
def sample(a,b,c):
    print(a,b,c)
sample(b=77,a=55,c=87)

#arbitary arguments
def sample(*a):
    print(a)
sample("hello",8,89.6)

def sample(**a):
    print(a)
sample(greet="hello",name="udayasree")


#void functions
def sample():
    print("hello world")
    return
sample()

#lambda functions
demo=lambda x,y:x+y
print(demo(1,2))"""
"""
def rem(a,b):
    print(a%b)
rem(2,4)

def rem(b,a):
    print(a%b)
rem(2,4)
"""

def rem(a,b):
    print(a%b)
rem(2,4)

def rem(b,a):
    print(a%b)
rem(2,4)
