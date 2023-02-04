# 1. Declare your age as integer variable
my_age = int(29)

# 2. Declare your height as a float variable
my_height = float(186.0)

# 3. Declare a variable that store a complex number
complx_var = 3 + 4j

'''
    4. Write a script that prompts the user to enter base 
    and height of the triangle and calculate an area of 
    this triangle (area = 0.5 x b x h).
'''
base = input('Enter Base of the Triangle')
height = input('Enter height of the Triangle')

area_of_triangle = 0.5 * base * height

#print(area_of_triangle)

'''
    5. Write a script that prompts the user to enter side a, 
    side b, and side c of the triangle. 
    Calculate the perimeter of the triangle (perimeter = a + b + c).
'''
a = input('Enter side a of the Triangle')
b = input('Enter side b of the Triangle')
c = input('Enter side c of the Triangle')

perimeter_of_triangle = a + b + c

#print(perimeter_of_triangle)

'''
    6. Get length and width of a rectangle using prompt. 
    Calculate its area (area = length x width) 
    and perimeter (perimeter = 2 x (length + width))
'''

length = input('Enter length of the rectangle')
width = input('Enter width of the rectangle')

area_of_rectangle = length * width

perimeter_of_rectangle = 2 * (length + width)

#print(area_of_rectangle)
#print(perimeter_of_rectangle)


'''
    7. Get radius of a circle using prompt. 
    Calculate the area (area = pi x r x r) 
    and circumference (c = 2 x pi x r) where pi = 3.14.
'''
pi = float(3.14)
radius = input('Enter radius of the circle')

area_of_circle = pi * radius**2

circumference_of_circle = 2 * pi * radius

'''
    8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
'''

slope8 = 2







'''
    9. Slope is (m = y2-y1/x2-x1).
    Find the slope and Euclidean distance between point (2, 2) 
    and point (6,10)

'''
x1, x2, y1, y2 = 2, 6, 2, 10
slope9 = ((y2 - y1) / (x2 - x1))
Euclidean_distance = (((y2 - y1)**2) - ((x2 - x1)**2))**0.5

print('The slope is ', slope9)
print('The Euclidean distance is', Euclidean_distance)

'''
    10. Compare the slopes in tasks 8 and 9.
'''
print(slope9 == slope8)

'''
    11. Calculate the value of y (y = x^2 + 6x + 9). 
    Try to use different x values and figure out 
    at what x value y is going to be 0.

'''
#x = input('Enter the value of x')

x = -3
y_value = x**2 + 6*x + 9

print(y_value)

'''
    12. Find the length of 'python' and 'dragon' 
    and make a falsy comparison statement.
'''

print(len('python'))
print(len('dragon'))

print(len('python') != len('python'))


'''
    13. Use an operator to check if 'on' is found
    in both 'python' and 'dragon'
'''
print('on' in 'python' and 'on' in 'dragon')


'''
    14. I hope this course is not full of jargon. 
    Use in operator to check if jargon is in the sentence.
'''

print('jargon' in 'I hope this course is not full of jargon.')


'''
    15. There is no 'on' in both dragon and python

'''





'''
    16. Find the length of the text python 
    and convert the value to float and convert it to string

'''

p = float(len('python'))
print(p)


'''
Even numbers are divisible by 2 and the remainder is zero. 
How do you check if a number is even or not using python?

'''
x = 8

# print(x % 2 == 0)

if (x % 2 == 0):
    print('Is Even Number')
else:
    print('Is Not Even Number')

'''
    18. Check if the floor division of 7 by 3 is equal
    to the int converted value of 2.7

'''
print(7 // 3 == int(2.7))


'''
Check if type of '10' is equal to type of 10
'''

print(type('10') == type(10))

'''
    20. Check if int('9.8') is equal to 10

'''
print(type(int('10')) == type(10))


'''
    21. Write a script that prompts the user 
    to enter hours and rate per hour. Calculate pay of the person
'''

hours = input('Enter hours:')
rate_per_hour =  input('Enter rate per hour:')

weekly_earning = hours * rate_per_hour

print('Your Weekly Earning is ', weekly_earning)


'''
    22. Write a script that prompts the user to enter number of years. 
    Calculate the number of seconds a person can live. 
    Assume a person can live hundred years
'''

Age = input('How Old Are You')
age_in_sec = Age * (60**2 * 24 * 365)

print('You have lived for {} seconds'.format(age_in_sec))


'''
    23. Write a Python script that displays the following table
'''
print(1, 1**0, 1**2, 1**3, 1**4)
print(2, 2**0, 2**2, 2**3, 2**4)
print(3, 3**0, 3**2, 3**3, 3**4)
print(4, 4**0, 4**2, 4**3, 4**4)
print(5, 5**0, 5**2, 5**3, 5**4)
