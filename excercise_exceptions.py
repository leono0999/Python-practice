# Starter code
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except: 
    print("The index does not exist in the list.")

# Starter code
def divide_by(a, b):
    return a / b
try:
    ans = divide_by(10, 0)
except:
    print("Error: Division by zero is not allowed.")


# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  