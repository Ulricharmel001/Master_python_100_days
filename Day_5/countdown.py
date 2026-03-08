# countdown 

import  time 
import math
# get input
start = int(input("Enter a Number start the countdown!\n"))
timer_speed = int(input("Enter your timer speed\n"))
half_way = start // 2
real_half_way = math.floor(half_way)


while start > 0:
    print(start)
    time.sleep(timer_speed)
    start -= 1
    if start == real_half_way:
        print(" Wow you are half way the coundown")
print("Happy New year")