list1=[1,2,3,4,5]
print (list1)
list2=[1,2,3,4,5]
print (*list2)
list3=[1,2,3,4,5]
print(list3, sep=" ")
list4=[1,2,3,4,5]
#list4.insert(len(list4),6)
#list4.append(3)
list4.extend([6,7,8])
print(list4, sep=" ")
del list4[0]
#list4.pop(0)
print(list4)

for x in list4:
    print('value:', x)

list5=[1,2,3,4,5]
print(len(list5))
list5.insert(len(list5)-3,6)
print(list5)