'''
    Exercises: Level 1
'''
# Create an empty tuple

family_member = ()
print(type(family_member))


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sisters_name = ('Husna', 'Aisha', 'Salma', 'Hauwa', 'Nana')
brothers_name = ('Danju', 'Kamal', 'Jamil', 'Deen')

#siblings = sisters_name + brothers_name
#print(siblings)




# Join brothers and sisters tuples and assign it to siblings

sisters_name = ('Husna', 'Aisha', 'Salma', 'Hauwa', 'Nana')
brothers_name = ('Danju', 'Kamal', 'Jamil', 'Deen')

siblings = sisters_name + brothers_name
print(siblings)



# How many siblings do you have?

sisters_name = ('Husna', 'Aisha', 'Salma', 'Hauwa', 'Nana')
brothers_name = ('Danju', 'Kamal', 'Jamil', 'Deen')

siblings = sisters_name + brothers_name
print(len(siblings))


# Modify the siblings tuple and add the name of your father and mother and assign it to family_members


sisters_name = ('Husna', 'Aisha', 'Salma', 'Hauwa', 'Nana')
brothers_name = ('Danju', 'Kamal', 'Jamil', 'Deen')

siblings = sisters_name + brothers_name

family_members = list(siblings)

family_members.insert(0, 'Abdullah')
family_members.insert(1, 'Zainab')

#family_members = siblings

family_members = tuple(family_members)
print(family_members)







'''
    Exercises: Level 2
'''
# Unpack siblings and parents from family_members

sisters_name = ('Husna', 'Aisha', 'Salma', 'Hauwa', 'Nana')
brothers_name = ('Danju', 'Kamal', 'Jamil', 'Deen')

siblings = sisters_name + brothers_name

family_members = list(siblings)

family_members.insert(0, 'Abdullah')
family_members.insert(1, 'Zainab')

#family_members = siblings

family_members = tuple(family_members)

father_name, mother_name, *siblings = family_members
print(siblings)






# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Oranges', 'Banana', 'Apple', 'Peach', 'Cherry', 'Kiwi')

vegetables = ('Onion', 'Peas', 'Cabbage', 'Pumpkin', 'Spinach', 'Corn')

animal_products = ('Meat', 'Milk', 'Egg', 'Cheese', 'Butter', 'Oil')

food_stuff_tp = fruits + vegetables + animal_products

print(len(food_stuff_tp))
print(food_stuff_tp)


# Change the about food_stuff_tp tuple to a food_stuff_lt list
fruits = ('Oranges', 'Banana', 'Apple', 'Peach', 'Cherry', 'Kiwi')

vegetables = ('Onion', 'Peas', 'Cabbage', 'Pumpkin', 'Spinach', 'Corn')

animal_products = ('Meat', 'Milk', 'Egg', 'Cheese', 'Butter', 'Oil')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = food_stuff_tp

print(food_stuff_lt)



# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.


fruits = ('Oranges', 'Banana', 'Apple', 'Peach', 'Cherry', 'Kiwi')

vegetables = ('Onion', 'Peas', 'Cabbage', 'Pumpkin', 'Spinach', 'Corn')

animal_products = ('Meat', 'Milk', 'Egg', 'Cheese', 'Butter', 'Oil')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_mid = food_stuff_tp[9:10]

print(food_stuff_mid)






# Slice out the first three items and the last three items from food_staff_lt list

fruits = ('Oranges', 'Banana', 'Apple', 'Peach', 'Cherry', 'Kiwi')

vegetables = ('Onion', 'Peas', 'Cabbage', 'Pumpkin', 'Spinach', 'Corn')

animal_products = ('Meat', 'Milk', 'Egg', 'Cheese', 'Butter', 'Oil')

food_stuff_tp = fruits + vegetables + animal_products

food_staff_lt = food_stuff_tp[:3] + food_stuff_tp[-3: ]

#food_staff_lt = food_stuff_tp[-3: ]

print(len(food_staff_lt))
print(food_staff_lt)





# Delete the food_staff_tp tuple completely

fruits = ('Oranges', 'Banana', 'Apple', 'Peach', 'Cherry', 'Kiwi')

vegetables = ('Onion', 'Peas', 'Cabbage', 'Pumpkin', 'Spinach', 'Corn')

animal_products = ('Meat', 'Milk', 'Egg', 'Cheese', 'Butter', 'Oil')

food_stuff_tp = fruits + vegetables + animal_products

#food_stuff_lt = food_stuff_tp

del food_stuff_tp



print(food_stuff_tp)






'''
    7.Check if an item exists in tuple:
   
'''
#  Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Sweden' in nordic_countries)


# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')


print('Iceland' in nordic_countries)

