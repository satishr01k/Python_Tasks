# 5.   Write a program in Python which will find all such numbers
# which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.


x=2000
#while x<=3200: # or we can also use the while loop
for x in range(2000,3200):
    if x%7 ==0 and x%5 != 0:
        print(x)
    x = x + 1

