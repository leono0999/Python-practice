def sum_of (**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v 
    return sum 
print (sum_of(coffee=2.23, cake=3.43, juice=1.23))