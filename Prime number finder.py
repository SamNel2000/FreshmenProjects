#first iteration around 30 seconds (to 10000)
#second iteration around 20 seconds
#third iteration around 6 seconds
#fourth iteration around 5 seconds
#fifth iteration around 4 seconds  (started to lag)
#sixth iteration around 6 seconds (apparently this change will produce faster results with larger numbers)
#fifth iteration test (50001 - 100k) 96 seconds
#sixth iteration test (50001 - 100k) 15 seconds the first time, 16 seconds the second, and it increasing slightly as it's lagged because of all the values in the shell

import math
#set composite to false if you only want primes printed and vice versa
booleanList = [ ]
upper_bound = 100
for n in range(3, upper_bound, 2):
    for k in range(3, int(math.sqrt(upper_bound)) + 1, 2):
        x = n / k
        if x == int(x):
            booleanList.append(True)
            break
    if True in booleanList:
        None
    else:
        print(n, "is prime")
    booleanList = []
        
    