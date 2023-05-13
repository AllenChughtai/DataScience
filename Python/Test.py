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
print("The change in estimated insurance cost for being male instead of female "+ str(change_in_insurance_cost))

#Functions

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

#Want to return max,min,round price of gift shop items
gift_shop_list = [tshirt_price,shorts_price,mug_price,poster_price]
max_price = (max(gift_shop_list))
#max_price = (max(tshirt_price,shorts_price,mug_price,poster_price))
min_price = (min(gift_shop_list))
rounded_price = (round(tshirt_price,1))

print(max_price)
print(min_price)
print(rounded_price)

#Variable Access
# Variable has been taken outside of a function and made global
# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

# Returns
current_budget = 3500.75
shirt_expense = 9


def deduct_expense(budget,expense):
  return (budget-expense)

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))
print_remaining_budget(current_budget)

new_budget_after_shirt = deduct_expense(current_budget,shirt_expense)

print_remaining_budget(new_budget_after_shirt)

# Mutiple Returns
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first,second,third

#The return values are bing associated to the following variables.
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(top_tourist_locations_italy())
print(most_popular1)
print(most_popular2)
print(most_popular3)

#Review

def trip_planner_welcome(name):
  print("Welcome to tripplaner v1.0" + str(name))

trip_planner_welcome("Allen")
