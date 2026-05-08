import time 
start_time = time.time()
#outer loop
for i in range(1000*1000):
    #inner loop
    for j in range(10):
        print(0, end=" ")
    print()
print (round((time.time() - start_time), 2))


