x=input('enter a number: ')

try:
    x=int(x)
    if (x % 3 == 0 and x % 5 == 0):
        print('Consultadd Python Training')
    elif x % 3 == 0:
        print('Consultadd')
    elif x % 5 == 0:
        print('c')
except:
    print('Enter a numeric value')


