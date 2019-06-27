import random
count = 1
while(count < 7):
    print(random.randrange(1,7))
    print("Do you want to roll again? 1:Yes, 2:No")
    x = input()
    if x == 1:
        print(random.randrange(1,7))        
    elif x == 2:
        break
    count+=1