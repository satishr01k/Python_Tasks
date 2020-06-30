x=input('Enter a age: ')

x= int(x)
if x>=11:
    print('you are eligible for the football match')
    if x<=20 or x>=60:
        print('Ticket price is $12')
    else:
        print('Ticket price is $20')


else:
    print('You are not eligible to buy a ticket')