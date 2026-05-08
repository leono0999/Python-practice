my_d ={1: 'hello', 'Name': 'john' , 2: 'bye'}
my_d[1] = 'hi'
my_d[4]= 'no worries'
del my_d[1] 
#print(my_d)

for key,value in my_d.items():
    print(str(key) + " : " + value)

