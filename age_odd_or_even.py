# prompt the user for input and convert the type to int
age = int(input('Enter Your Age: '))
# perform modulo operation to determine if number if even
if age % 2 == 0:
    print('Your age is even')
else:
    print('Your age is odd')