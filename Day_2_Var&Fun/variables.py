# Exercise: Level 1

# Day 2: 30 Days of python programming
first_name = 'Kabila'
last_name = 'Musa'
full_name = first_name + ' '+ last_name
country_name = 'Nigeria'
city = 'Kano'
age = 29
year = 2023
is_married = True
is_true = True
is_light_on = is_true
name, school, fruit, color, car = 'Abdullahi', 'Al-Azhar', 'Orange', 'Blue', 'Benz'

# Exercise: Level 2

# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country_name))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))


# 3. Compare the length of your first name and your last name
print(len(first_name) == len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

num_tot = num_one + num_two
num_diff = num_one - num_two
num_mul = num_one * num_two
num_div = num_one / num_two
num_mod = num_one % num_two
num_exp = num_one ** num_two
num_flr = num_one // num_two

print(num_tot)

'''
    5. The radius of a circle is 30 meters.
    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area.

'''

radius = 30
pi = 3.14
#radius = int(input('Enter radius'))

# i.
Area_of_circle = pi * (radius)**2

print(Area_of_circle)

#ii
circum_of_circle = 2 * pi * 30

print(circum_of_circle)

#iii
pi = 3.14
radius = float(input('Enter radius'))

Area_of_circle = pi * (radius)**2

circum_of_circle = 2 * pi * radius

#print(Area_of_circle)
#print(circum_of_circle)

'''
    6. Use the built-in input function to get 
    first name, last name, country and age 
    from a user and store the value to their corresponding variable names

'''
First_name = str(input('Enter Your First Name'))
Last_name = str(input('Enter Your Last Name'))
Country = str(input('Enter Your Country Name'))
Age = int(input('Enter Your Age'))


'''
Run help('keywords') in Python shell 
or in your file to check for the Python reserved words or keywords

'''
print(help('keywords'))
