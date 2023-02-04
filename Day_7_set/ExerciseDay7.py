'''
    Exercises: Level 1
'''
# 1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


print(len(it_companies))


# 2. Add 'Twitter' to it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies.add('Twitter')

print(len(it_companies))
print(it_companies)


# 3. Insert multiple IT companies at once to the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies_upd = {'Twitter','Hauwei', 'AliBaBA', 'WeChat'}

it_companies.update(it_companies_upd)

print(len(it_companies))
print(it_companies)



# 4. Remove one of the companies from the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies.remove('IBM')

print(len(it_companies))
print(it_companies)


# 5. What is the difference between remove and discard

'''
    The discard() method will not raise an error 
    if the item is not in the set WHILE delete() will 
    raise an error if the the item is not in the set. 
    
'''



'''
    Exercises: Level 2
'''
# 1. Join A and B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

print(C)

# 2. Find A intersection B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.intersection(B)

print(C)



# 3. Is A subset of B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.issubset(B)

print(C)



# 4. Are A and B disjoint sets

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.isdisjoint(B)

print(C)




# 5. Join A with B and B with A

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

D = B.union(A)

print(C)
print(D)


# 6. What is the symmetric difference between A and B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.symmetric_difference(B)

print(C)



# 7. Delete the sets completely

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

del C
print(C)



'''
    Exercises: Level 3
'''
# 1. Convert the ages to a set and compare 
#   the length of the list and the set, which one is bigger?

age = [22, 19, 24, 25, 26, 24, 25, 24]

age_lst_ln = len(age)


age_st = set(age)
age_st_ln = len(age_st)

print(age_lst_ln)
print(age_st_ln)
print(len(age) == len(age_st))

# 2. Explain the difference between the following data types: 
#      string, list, tuple and set

'''
    string: 

    list:

    tuple:

    set:

'''


# 3. I am a teacher and I love to inspire and teach people. 
#   How many unique words have been used in the sentence? 
#   Use the split methods and set to get the unique words.

sentence = 'I am a teacher and I love to inspire and teach people'

sentence = sentence.split() # split() method convert string to list

#print(type(sentence))
#print(len(sentence))
#print(sentence)

sentence_st = set(sentence)

#print(len(sentence_st))
#print(type(sentence_st))
#print(sentence_st)

print(len(sentence))
print(len(sentence_st))
print(len(sentence) == len(sentence_st))





