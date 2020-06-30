x="satish123"

y=list(x)
print(y)
print(y[1])
print(type(y[7]))

y=x.split(" ")
print(y)

for letter in y:
    if letter==int(letter):
        print(letter)

# for letter in "satish123":
#     if letter in range(10):
#         print(letter)
