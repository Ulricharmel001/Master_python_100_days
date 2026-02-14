# for loop

#for variable in (start, stop, step)

for i  in range(5, 0, -1):
    print(i)

#while loop 
# repeat untill the condition is false 

count = 0
while count <5:
    print(count)
    count += 1

    # time : to simimulate real time processes

import time 

for item in range(5, 0, -1):
    print(item)
    time.sleep(2)
print("Happy new year")