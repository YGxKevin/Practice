# this is a BMI calculator practice.
print('Hi This is a BMI calculator')
name = input('name: ')
height = input('height(m): ')
weight = input('weight(kg): ')
height = float(height)
weight = float(weight)
bmi = weight / (height*height)
if bmi < 18.5:
	print('your bmi is too low.')
elif 18.5 <= bmi < 25:
	print('your bmi is normal.')
elif bmi >= 25:
	print('your bmi is too high.')
else:
	print('please reenter valid figure)
