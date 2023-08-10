#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
test = int(str(number)[-1])
print("Last digit of {} is {} ".format(number,test),end="")
if test > 5:
    print("and is greater than 5")
elif test < 6 and test != 0:
    print("and is less than 6 and not 0")
elif test == 0:
    print("and is 0")
