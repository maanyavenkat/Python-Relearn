print("hello world")

# name = "Tim" #string
# age = 26. #integer
# height = 5.9 #float
# is_learning = True #boolean

# print(name, "is", age, "years old and is", height, "feet tall.")
# print (type(name))

#concatenation
# first_name = "Maanya"
# last_name = "Venkat"
# print(first_name + " " + last_name) # can also use commas to seperate

# # or use an f string
# message = f"Hi my name is {first_name} {last_name} and I am {age} years old."
# print(message)


# #input function -- think sout print without the ln in java
# user_name = input ("what is your name? ")
# print("Hello," , user_name + "!")

# #in order to do the input function with integers or floats, need to convert the input to the correct type
# user_age = int(input("How old are you? "))
# user_height = float(input("How tall are you? "))
# print("You are", user_age, "years old and", user_height, "feet tall.")

# #lists
# groceries = ["apples", "bananas", "milk"] 
# print(groceries[2])
# groceries.append("eggs") #adds to the end of the list
# print(len(groceries))


# #conditionals
# age = 179

# if age >= 65:
#     print("senior")
# elif age >= 18:    #same as else if in java
#     print("adult")
# else:
#     print("minor")

# #for loops
# groceries = ["apples", "bananas", "milk"] 

# for item in groceries:  #item = variable that holds values in list; groceries = list
#         print(item)


# #or can loop based on number
# for number in range(5)
#     print(number) #prints 0-4, range is exclusive of the last number


# #functions -- make your own!
# def greet(name):  # name is a parameter that is passed into the function
#     print(f"Hello, {name}!")

# greet("Tim") # tim is the argument that is passed into the function
# greet("Joe")
# greet("sarah")

# def add (a,b):
#     return a+b

# result = add(5,3)
# print(result)

#example program

def calculate_tip(bill, percent):
    tip = bill * (percent/100)
    return tip

bill_amount = float(input("What was your bill? "))
tip_percent = float(input("What percent do you want to tip? "))

tip = calculate_tip(bill_amount, tip_percent)
total = bill_amount + tip

print(f"Tip amount: ${tip}")
print(f"Total to pay : ${total}")
    
