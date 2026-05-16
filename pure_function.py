soccer = [2,4,5,5]

def pure_function(item):
    soccer.append(item)
    return soccer

newlist= pure_function(4)
print(soccer)
print(newlist)

def pure_function(item):
    return soccer.append(item) 

newlist= pure_function(4)
print(soccer)
print(newlist)

my_list= [1,2,3]

def add_to_list(lst,item):
    lst.append(item)
    return lst

newlist= add_to_list(my_list, 4)
print(my_list)
print(newlist)

my_list = [1,2,3]

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)