# for x in range(6):
#     if x ==3:
#         continue
#         print(x)
# x= input('Enter a number: ')
# x=int(x)
x=0
y=''
while x>=0 and x<=6:
    if x==3 or x==6:
        x = x + 1
        continue
    y=y +str(x)+' '
    # print(x)
    x=x+1

print(y)
