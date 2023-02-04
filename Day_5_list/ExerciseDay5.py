'''
    1. Declare an empty list
'''

cars = []



'''
    2. Declare a list with more than 5 items
'''

cars = ['Honda', 'Benz', 'Ferarri', 'Tesla', 'Nissan']



'''
    3. Find the length of your list
'''

print(len(cars))


'''
    4. Get the first item, the middle item and the last item of the list
'''
cars = ['Honda', 'Benz', 'Ferarri', 'Tesla', 'Nissan']

first_car = cars[0]
middle_car = cars[2]
last_car =cars[-1]

print('Fisrt Car is', first_car)
print('Middle Car is', middle_car)
print('Last Car is', last_car)


'''
    5. Declare a list called mixed_data_types, 
    put your(name, age, height, marital status, address)
'''
#mixed_data_types = ['Kabila', 29, 189, 'Married', 'Kano']
mixed_data_types = ('Kabila', 29, 189, 'Married', 'Kano')

mixed_data_types = list(mixed_data_types)
print(type(mixed_data_types))
print(len(mixed_data_types))


'''
    6. Declare a list variable named it_companies and assign initial 
    values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' 'Amazon']


'''
    7. Print the list using print()
'''

print(it_companies)



'''
    8. Print the number of companies in the list
'''

print(len(it_companies))





'''
    9. Print the first, middle and last company
'''
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]

print('First company is', first_company)
print('Middle company is', middle_company)
print('Last company is', last_company)

'''
    10. Print the list after modifying one of the companies
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies[0] = 'Hauwei'

print(it_companies)


'''
    11. Add an IT company to it_companies
'''
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.append('Hauwei')

print(it_companies)


'''
    12. Insert an IT company in the middle of the companies list
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.insert(3, 'Hauwei')

print(it_companies)


'''
    13. Change one of the it_companies names to uppercase (IBM excluded!)
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies[0] = 'FACEBOOK'

print(it_companies)


'''
    14. Join the it_companies with a string '#;  '
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

strg = ['#']

it_companies = it_companies + strg

print(it_companies)


'''
    15. Check if a certain company exists in the it_companies list.
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print('Amazon' in it_companies)




'''
    16. Sort the list using sort() method
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.sort()

print(it_companies)



'''
    17. Reverse the list in descending order using reverse() method
'''
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.reverse()

print(it_companies)


'''
    18. Slice out the first 3 companies from the list
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

first_three = it_companies[0:3]

print(first_three)


'''
    19. Slice out the last 3 companies from the list
'''


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

last_three = it_companies[4:]

print(last_three)







'''
    20. Slice out the middle IT company or companies from the list
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

middle_it_company = it_companies[3]

print(middle_it_company)

'''
    21. Remove the first IT company from the list
'''


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.remove('Facebook')

print(it_companies)


'''
    22. Remove the middle IT company or companies from the list
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

del it_companies[3]

print(it_companies)






'''
    23. Remove the last IT company from the list
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.pop()

print(it_companies)



'''
    24. Remove all IT companies from the list
'''
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.clear()

print(it_companies)




'''
    25. Destroy the IT companies list
'''

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

del it_companies

print(it_companies)




'''
    26. Join the following lists:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
'''

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']

back_end = ['Node','Express', 'MongoDB']

developers = front_end + back_end

print(developers)



'''
    27. After joining the lists in question 26. 
    Copy the joined list and assign it to a variable full_stack. 
    Then insert Python and SQL after Redux.
'''

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']

back_end = ['Node','Express', 'MongoDB']

developers = front_end + back_end

full_stack = developers.copy()

#new_list = ['Python', 'SQL']


full_stack.insert(5, 'Python')

full_stack.insert(6, 'SQL')

print(full_stack)




#Exercises: Level 2

'''
    1. The following is a list of 10 students ages:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
'''

#Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(ages)



#Add the min age and the max age again to the list


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

min_age = min(ages)

max_age = max(ages)

sum_tot = max_age + min_age

ages.append(sum_tot)

print(ages)





#Find the median age (one middle item or two middle items divided by two)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

list_len = len(ages)

if list_len % 2 == 0:
    mid1 = ages[list_len//2]
    mid2 = ages[list_len//2 - 1]
    
    median_age = (mid1 + mid2) / 2

else:
    median_age = ages[list_len//2]


print(ages)
print(mid1, mid2, median_age)






#Find the average age (sum of all items divided by their number )

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

list_len = len(ages)

sum_num = sum(ages)

average_age = sum_num / list_len

print(average_age)



#Find the range of the ages (max minus min)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


min_age = min(ages)
max_age = max(ages)

range_age = max_age - min_age

print(min_age, max_age, range_age)


#Compare the value of (min - average) and (max - average), 
# use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


list_len = len(ages)

sum_num = sum(ages)

average_age = sum_num / list_len



min_age = min(ages)
max_age = max(ages)

range_age = max_age - min_age

min_compare = abs(min_age - average_age)

max_compare = abs(max_age - average_age)

print(min_compare, max_compare, min_compare == max_compare)



''' 1. Find the middle country(ies) in the countries list
    ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
'''

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
#countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

len_country = len(countries)

if len_country % 2 == 0:
    mid_country1 = countries[len_country // 2]
    mid_country2 = countries[len_country // 2 - 1]

else:
    mid_country = countries[len_country // 2]

print(len(countries))
print(mid_country)



'''
    2. Divide the countries list into two equal lists
     if it is even if not one more country for the first half.
''' 

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

mid_num = 4

first_half = countries[ : mid_num]

second_half = countries[mid_num : ]

print(countries)
print(first_half)
print(second_half)

'''  3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
     Unpack the first three countries and the rest as scandic countries.
'''

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, second_country, third_country, *scandic = countries

print(scandic)





