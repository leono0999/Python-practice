file= open('file.txt', mode ='r')
data=file.readlines()
print(data)
file.close()

for dates in data:
    print(dates)

with open('file.txt' , mode ='r') as file:
    for x in file:
        print(x)
