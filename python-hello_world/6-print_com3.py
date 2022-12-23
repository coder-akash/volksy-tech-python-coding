#!/usr/bin/python3
for i in range(1, 10):
    print("{:02d}".format(i), end=", ")
for i in range(10,100):
    if i != int(str(i)[::-1]):
        if i < int(str(i)[::-1]):
            if i == 89:
                print(i)
             else:
                print('{}'.format(i), end = ", ")
