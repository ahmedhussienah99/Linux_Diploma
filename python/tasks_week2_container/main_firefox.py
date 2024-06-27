

import firelink


print("you can choose your website from lis :")
print("1-google") 
print("2-w3school") 
print("3-youtube") 
print("4-facebook") 
# note for you the input take input with string type
link = input() 

if link =='1' :
    firelink.firefox(firelink.url[0])
if link =='2' :
    firelink.firefox(firelink.url[1])
if link =='3' :
    firelink.firefox(firelink.url[2])
if link =='4' :
    firelink.firefox(firelink.url[3])