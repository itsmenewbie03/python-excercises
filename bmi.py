weight =  float(input('Enter Your Weight in KG: '))
height = float(input('Enter Your Height in Meters: '))
bmi = weight / (height * height)
print(f'Your BMI is: {bmi}')

if bmi < 18.5:
    print('You are UNDERWEIGHT')
elif bmi >= 18.5 and bmi <= 24.9:
    print('You have NORMAL WEIGHT')
else:
    print('You are OVERWEIGHT') 