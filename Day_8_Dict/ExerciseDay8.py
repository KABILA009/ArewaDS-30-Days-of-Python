# 1. Create an empty dictionary called dog
dog = {}


# 2. Add name, color, breed, legs, age to the dog dictionary

dog = {}
dog['name'] = 'Tracy'
dog['breed'] = 'Bulldog'
dog['legs'] = 4
dog['age'] = 10

print(type(dog))
print(len(dog))
print(dog.get('breed'))
print(dog)

# 3. Create a student dictionary and add first_name, last_name, 
#    gender, age, marital status, skills, country, 
#    city and address as keys for the dictionary

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }




# 4. Get the length of the student dictionary

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }


print(len(student))
print(student.get('address'))


# 5. Get the value of skills and check the data type, it should be a list

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }


std_skl = student.get('skills')

print(type(std_skl))
print(std_skl[0])
print(std_skl)



# 6. Modify the skills values by adding one or two skills

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }

student['skills'].append('Visual Basic') 

print(student)



# 7. Get the dictionary keys as a list

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }

student_keys = student.keys()

print(student_keys)



# 8. Get the dictionary values as a list

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }

student_val = student.values()

print(student_val)



# 9. Change the dictionary to a list of tuples using items() method


student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }

student_itm = student.items()

print(student_itm)



# 10. Delete one of the items in the dictionary

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }

#del student['age']
student.pop('marital_status')
print(student)



# 11. Delete one of the dictionaries

student = {
            'first_name' : 'Kabila',
            'last_name' : 'Musa',
            'gender' : 'Male',
            'age' : 29 ,
            'marital_status' : 'Married',
            'skills' : ['Python', 'SQL', 'HTML', 'Java'],
            'country' : 'Nigeria',
            'city' : 'Kano',
            'address' : '58 Gwarzo RD'
        }

del student

print(student)
