#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
ln= n % 10
if n > 0:
    if ln == 0:
        print("Last digit of {} is {} and is 0".format(n, ln))
    elif ln > 5:
        print("Last digit of {} is {} and is greater than 5".format(n, ln))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(n, ln))
else:
    ln= int(str(n)[-1])
    if ln == 0:
        print("Last digit of {} is {} and is 0".format(n, ln))
    else:
        print("Last digit of {} is -{} and is less than 6 and not 0".format(n, ln))
