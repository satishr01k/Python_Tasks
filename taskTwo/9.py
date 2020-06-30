y=254 ## takign a random lucky number

answer='yes'
x=5
x=input('Guess the lucky number: ')

x=int(x)

print(x)
print(y)

while x!=y and answer!='no':
    answer = input('would you like to continue: ')
    if answer=='no':
        break
    x=input('Guess the lucky number: ')
    x = int(x)




