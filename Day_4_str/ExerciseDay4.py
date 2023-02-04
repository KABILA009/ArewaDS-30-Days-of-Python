'''
    1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' 
    to a single string, 'Thirty Days Of Python'.

'''
single_string1 = 'Thirty' + ' ' + 'Days' + ' ' +  'Of'+ ' ' +  'Python' 
print(single_string1)



'''
    2. Concatenate the string 'Coding', 'For' , 'All' to a 
    single string, 'Coding For All'.
'''
single_string2 = 'Coding' + ' ' + 'For' + ' ' +  'All' 
print(single_string2)



'''
    3. Declare a variable named company and 
    assign it to an initial value "Coding For All".
'''

company = "Coding For All"
#print(company)




'''
    4. Print the variable company using print().
'''
company = "Coding For All"
print(company)



'''
    5. Print the length of the company string 
    using len() method and print().
'''

company = "Coding For All"
print(len(company))





'''
    6. Change all the characters to uppercase letters 
    using upper() method.
'''

company = "Coding For All"
print(company.upper())




'''
    7. Change all the characters to lowercase letters 
    using lower() method.
'''

company = "Coding For All"
print(company.lower())



'''
    8. Use capitalize(), title(), swapcase() methods 
    to format the value of the string Coding For All.
'''

company = "Coding For All"

print(company.capitalize())
print(company.title())
print(company.swapcase())





'''
    9. Cut(slice) out the first word of Coding For All string.
'''
company = "Coding For All"

print(company[0])





'''
    10. Check if Coding For All string contains a word Coding 
    using the method index, find or other methods.
'''
company = "Coding For All"

print('Coding' in company)



'''
    11. Replace the word coding in the string 'Coding For All' 
    to Python.
'''

company = "Coding For All"

print(company.replace('Coding', 'Python'))


'''
    12. Change Python for Everyone to Python for All 
    using the replace method or other methods.
'''

company = "Python for Everyone"

print(company)
print(company.replace('Everyone', 'All'))




'''
    13. Split the string 'Coding For All' using space 
    as the separator (split()) .
'''

company = "Coding for All"

print(company)
print(company.split(' '))
print(company.split())

'''
    14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, 
    Amazon" split the string at the comma.
'''

tech_company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(tech_company.split(','))

'''
    15. What is the character at index 0 in the string 
    Coding For All.
'''

company = "Coding for All"

print(company[0])



'''
    16. What is the last index of the string Coding For All.
'''
company = "Coding for All"

last_index = len(company) - 1

print(last_index)

print(company.rfind('l'))

print(last_index == company.rfind('l'))



'''
    17. What character is at index 10 in "Coding For All" string.
'''

company = "Coding for All"

print(company[10])


'''
    18. Create an acronym or an abbreviation for the name 
    'Python For Everyone'.
'''

company = "Python For Everyone"

acronym = company[0:18:7]

print(acronym)




'''
    19. Create an acronym or an abbreviation for the name 
    'Coding For All'.
'''
company = "Python For All"

acronym = company[0:13:4]

print(acronym)




'''
    20. Use index to determine the position of the 
    first occurrence of C in Coding For All.
'''

company = "Coding For All"


print(company.find('C'))



'''
    21. Use index to determine the position of the 
    first occurrence of F in Coding For All.
'''
company = "Coding For All"


print(company.find('F'))



'''
    22. Use rfind to determine the position of the 
    last occurrence of l in Coding For All People.
'''

company = "Coding For All"


print(company.rfind('l'))




'''
    23. Use index or find to find the position of the 
    first occurrence of the word 'because' in the following sentence: 
    'You cannot end a sentence with because because because is a conjunction'
'''

sentence = "You cannot end a sentence with because because because is a conjunction"


print(sentence.find('because'))





'''
    24. Use rindex to find the position of the last occurrence 
    of the word because in the following sentence: 
    'You cannot end a sentence with because because because is 
    a conjunction'
'''

sentence = "You cannot end a sentence with because because because is a conjunction"


print(sentence.rfind('because'))





'''
    25. Slice out the phrase 'because because because' in the 
    following sentence: 
    'You cannot end a sentence with because because because is 
    a conjunction'
'''

sentence = "You cannot end a sentence with because because because is a conjunction"

print(sentence.strip('because because because'))



'''
    26. Find the position of the first occurrence of 
    the word 'because' in the following sentence: 
    'You cannot end a sentence with because because because is 
    a conjunction'
'''


sentence = "You cannot end a sentence with because because because is a conjunction"

print(sentence.find('because'))


'''
    27. Slice out the phrase 'because because because' in 
    the following sentence: 
    'You cannot end a sentence with because because because is 
    a conjunction'
'''
sentence = "You cannot end a sentence with because because because is a conjunction"

print(sentence.strip('because because because'))


'''
    28. Does 'Coding For All' start with a substring Coding?
'''

sentence = 'Coding For All'

print(sentence.startswith('Coding'))



'''
    29. Does 'Coding For All' end with a substring coding?
'''

sentence = 'Coding For All'

print(sentence.endswith('Coding'))







'''
    30. '   Coding For All      '  , remove the left and right 
    trailing spaces in the given string.
'''

sentence = '   Coding For All      '

print(sentence.strip())



'''
    31. Which one of the following variables 
    return True when we use the method isidentifier():
    30DaysOfPython
    thirty_days_of_python
'''


iden = 'thirty_days_of_python'
print(iden.isidentifier())


'''
    32. The following list contains the names 
    of some of python libraries: 
    ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
    Join the list with a hash with space string.
'''

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

result = ' '.join(python_libraries)
print(result)

'''
    33. Use the new line escape sequence to separate 
    the following sentences.
    I am enjoying this challenge.
    I just wonder what is next.
'''

print(' I \n am \n enjoying \n this \n challenge.')

print(' I \n just \n wonder \n what \n is \n next')





'''
    34. Use a tab escape sequence to write the following lines.
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
'''

print(' Name \t Age \t Country \t City \n Kabila \t 29 \t Nigeria \t kano')







'''
    35. Use the string formatting method to display the following:
    radius = 10
    area = 3.14 * radius ** 2
    The area of a circle with radius 10 is 314 meters square.
'''

radius = 10
area = int(3.14 * radius ** 2)

print('The area of a circle with radius {} is {} meters square.'.format(radius, area))






'''
    36. Make the following using string formatting methods:
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144
'''

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))




a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b : .2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')