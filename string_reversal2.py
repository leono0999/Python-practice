def streversal(str):
    if len(str) == 0:
        return str
    else:
        return streversal(str[1:]) + str[0] 
    
rev = 'reversal'
rev2= streversal(rev)
print(rev2)