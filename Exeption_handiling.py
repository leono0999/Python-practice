def division(a, b):
    d = a / b
    return d
try:
    ans = division(10,0)
except Exception as e:
    print('an error happended', e)
    print(e.__class__)

