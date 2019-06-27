import random
x = random.randrange(1,100)
print(x)
stop = False
while(stop == False):
    print("Please input a number: ")
    y1 = input()
    if (y1.isnumeric() and y1 != '-1'):
        y = int(y1) 
        if x < y:
            print("The number is too high. Type -1 if you wanna stop")
        elif x > y:
            print("The number is too low. Type -1 if you wanna stop")
        else:
            print("Correct. Congrats")
            break 
    elif y1 == '-1':
        break              