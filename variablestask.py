


#1.	Create three variables in a single line and assign different values to them and make sure their data types are different. Like one is int, another one is float and the last one is a string.
a, b, c=10, 11.5, 'satish'

print(a)
print(b)
print(c)


# 2. 	Create a variable of value type complex and swap it with another variable whose value is an integer.
x,y=10,2+7j
print(x)
print(y)
print(type(y))

x,y=y,x
print(x)
print(y)
print(type(y))

# 3. 	Swap two numbers using the third variable as the result name and do the same task without using any third variable.
x=10
y=20
z=0 #third variable
x,z=z,x
# print(x)
# print(z)
y,z=z,y
# print(y)
# print(z)
x,z=z,x

print(x)
print(y)
print(z)

#without third variable

x,y=y,x




# 4. 	Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

#python3
x=input('Enter a value: ')
print(x)

#python2

#x=raw_input('enter a value : ')
#print('x')


# 5. 	Write a program to complete the task given below:
# Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
# Use z for adding 30 into it and print the final result by using variable results.

x=input('Enter first number between 1-10: ')
y=input('Enter second number between 1-10: ')
#add exception handling. if number not in range or not int
z=int(x)+int(y)
z=z+30
print('final result: ' ,z)

# 6. 	Write a program to check the data type of the entered values.
# HINT: Printed output should say -  The input value data type is: int/float/string/etc
print(type(x))
print(type(y))


# 7. 	If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again.
# Will it change the value. If Yes then Why?

a=15
print('a before: ',a)
a='satish'
print('a after: ',a)

#Ans: Yes. It will change. because the value of a variable is mutable.
# after the value/data type is changed the new value is created in the memory and named as 'a'

