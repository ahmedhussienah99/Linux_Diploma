
DDRA=0
def get_value_reg():
    DDRA=0
    DDRAb=0
    for i in range(0,8) :
        bit_value=input(f"please enter Bit {i} mode : ").lower()
        if bit_value=='in':
            DDRA=DDRA&(~(1<<i))
        if bit_value=='out':
            DDRA=DDRA|((1<<i))
        #print(bin(DDRA))
    DDRAb=bin(DDRA)[2:].zfill(8)
    print("DDRA=0b"+DDRAb)

'''The [2:] slice notation is used to remove the leading 0b. The zfill(8) 
method adds leading zeros to pad the string to a length of 8 characters.
'''

get_value_reg()
