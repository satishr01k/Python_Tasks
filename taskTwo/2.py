print("If User Enter 1 - Addition\nIf User Enter 2 - Subtraction\nIf User Enter 3 - Division\nIf USer Enter 4 - Multiplication\nIf User Enter 5 - Average"
)

x=input('Enter a between 1 and 5 to perform the operation: ')

try:
    x= int(x)
    if x >= 1 and x <= 5:
        first = input('enter the first value: ')
        second = input('Enter the second value: ')
        try:
            first = int(first)
            second = int(second)
        except:
            'enter numeric values'
        if x == 1:
            ans = first + second
        elif x == 2:
            ans = first - second
        elif x == 3:
            ans = first / second
        elif x == 4:
            ans = first * second
        elif x == 5:
            first1 = input('Enter next set of 1st value: ')
            second1 = input('enter next set of 2nd value: ')
            try:
                first1 = int(first1)
                second1 = int(second1)
                ans = (first + first1 + second + second1) / 4
            except:
                print('Invalid entry, enter numeric second set of values:')
except:
    print('Invalid value, Enter a value between 1 and 5')


if float(ans)<=0:
    print(ans)
    print('Zsa')
else:
    print(ans)


