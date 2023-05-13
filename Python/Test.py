#Print Statement introductions
print("Hello World")

#Variable Introduction
meal = 'an english muffin'
print('For Breakfast I had: ' + meal)
meal = 'Pizza'
print('For Lunch I had: ' + meal)
meal ="Coffee"
print('For Dinner I had: ' + meal)

#Numbers Introductions
# int is a whole number: -3,2,-1,0,1,2,3
# float is a decimal number

#Calculations
# Mathematical operations in Python follow the standard mathematical order of operations
quick_math = (25*68+13/28)
print(quick_math)

#Variables that are assigned numeric values can be treated the same as the number themselves

quilt_width = 8
quilt_length = 12
print(quilt_width*quilt_length)

#Exponents
print(6**2) #6*6
print(7**2)
print(8**2)

#Modulo
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)

my_team = (27%4)

#Concatentation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

message = (string1+string2+string3+string4+string5+string6)

#PlusEquals, Python offers a shorthand for updating variables. When you have a number saved in a variable and want to add to the current value of the variable
hike_caption = "What an amazing time to walk through nature!"
hike_caption += " #nofilter"
hike_caption += " #blessed"
print(hike_caption)

#MultiLine String is ''' whole sentence can be written out '''

#Practice Variables and Concatenation
my_age = 25
half_my_age = 25/2
greeting = "Hi I'm,"
name = "Allen Chughtai"
greeting_with_name = greeting + " " +name

print(greeting_with_name)

# Medical Insurance Project
age = int
sex = int
bmi = float
num_of_children = int
smoker =  int

#Defining the variables of a 28 year old female who does not smoke, 3 children and BMI=26.2
age = 28
sex = 0
smoker = 0
bmi = 26.2
num_of_children = 3

#Insurance cost formula below
#str() function needed to change insurance_cost float to string for concatentation purposes
insurance_cost = 250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
print("This person's insurance cost is " +  str(insurance_cost) + " dollars")

#New insurance cost due to age adjustment
age += 4
new_insurance_cost = 250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost = new_insurance_cost-insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is "+ str(change_in_insurance_cost) + " dollars.")

age = 28
bmi += 3.1

new_insurance_cost = 250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
change_in_insurance_cost = new_insurance_cost-insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is "+ str(change_in_insurance_cost) + " dollars.")

bmi = 26.2
sex = 1

new_insurance_cost = 250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
change_in_insurance_cost = new_insurance_cost-insurance_cost
print("The change in estimated insurance cost for beiung male instead of female "+ str(change_in_insurance_cost))





