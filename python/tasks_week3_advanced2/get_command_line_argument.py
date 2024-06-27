import sys


print(f"this is the name/path of script : {sys.argv[0]} ")
length = len(sys.argv)
print(f"Number of arguments :{length}")

print("Argument List :[",end=" ")
for i in range(0,length) :

    if i !=length-1 :
        print(f'"{sys.argv[i]}"',end=",")
    if i ==length-1 :
        print(f'"{sys.argv[i]}"',end="")

print("]")
