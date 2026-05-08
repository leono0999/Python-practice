my_tuple =(2,"hello", True, 1.4,4)
print(my_tuple.count(4))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

#set1.add(5)
#set1.remove(3)
#set1.discard(2)
print(set2.union(set1))
#print(set1.intersection(set2))
#print(set1 & set2)
print(set1.difference(set2))
print(set1-set2)
print(set1.symmetric_difference(set2))