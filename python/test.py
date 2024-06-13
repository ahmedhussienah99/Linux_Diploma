import dis

#comment line1
'''
comment more line
'''

print("hello \nahmed")

x=4
y=3.5
print(type(x))
print(type(y))

# dynamic langague you can define variable more time
x=4
x=3.5
print(type(x))

#variable nameing no %x or 5y 
#name is case sensitive


#comma operator 
q,w,e=1,2,3
print(q)
print(w)
print(e)


#Data Types
#string
x="ahmed"
#int
x=5
#complex
x=5+3j


################### list ###################
'''
collection : you can put any data types together 
ordered    : it is ordered indexed 0 then 1 then 2 .... 
indexed    : it is indexed 
             you can see index like that
             [0,1,2] or [-3,-2,-1]
mutable    : you can change any value of any index in list
range      : you can use range [start:step:end]or [start] or [start:end] 
             if start = space you will start from first or end you will complete to last position
'''
x=["mo",1,2,3]
print(x[1:3])
print(x[1:1:3])

################### tuple ###################
'''
collection : you can put any data types together 
ordered    : it is ordered indexed 0 then 1 then 2 .... 
indexed    : it is indexed 
             you can see index like that
             [0,1,2] or [-3,-2,-1]
immutable    : you can not change any value of any index in tuple all variables are constant =define only one time 
range      : you can use range [start:step:end]or [start] or [start:end] 
             if start = space you will start from first or end you will complete to last position
'''

x=(1,2,3,4,5,6)
#x[1]=5 yo can not do that 
print(x[1:3])
print(x[1:2:5])

################### SET ###################
'''
collection : you can put any data types together and each value not have unique index sometimes 0 or 1 it i will change 
unordered    : it is unordered 
mutable    : you can  change any value 

Notes
1-you can not duplicatie values 
2-you can not print specific value like lis[0]
'''
lis={1,"ahmed"}
#print(lis[0])
print(lis)
################### Dictionary ###################
'''
DICT={
    "KEY":VALUE
}
collection : you can put any data types together 
ordered    : it is ordered by keys 
indexed    : it will indexed by yours keys 
mutable  : you can  change any value of any KEY

Notes
1-you can not do that 
    dictt=
    {
    }
2-each key has value and you can do any values like list or int or another dict
3-the key is unique 
'''
dictt={                     
                            
    "time":"5am",
    "year":2024

}
print("###############DICTIONARY######################")
print(dictt)
print(len(dictt))
print(dictt.keys())
print(dictt.values())
print(dictt["time"])


################### function range and creat list()###################
print("################### function range and creat list ###################")
y=list(range(0,10))
print(y)
r="ahmed"
print(list(r))              #convert string to list


################### INPUT and PRINT Variables ###################
name=input("enter name ")
x=5
print(f"your name:{name}")
print("your name:{} and x={}".format(name,x))

################### Operatos ###################
