str = 'racecar'
print(str[0])
print(str[6])

def ispalindrome(str):
    index_ini = 0
    index_end = len(str)-1
    for i in str:
        if str[index_ini] != str[index_end]:
            return False
    return True 

print(ispalindrome('racecars'))

