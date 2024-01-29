import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)

random_choice = random.randint(0, num_items-1)
person_who_will_pay = names [random_choice]
print(person_who_will_pay + "is going to buy the meal today!")

#test_seed = random.randint(0,10)
#if test_seed == 1 and 2:
#    print(f"names[0] is going to buy the meal today!")
#if test_seed == 3 and 4:
 #   print(f"names[1] is going to buy the meal today!")
#if test_seed == 5 and 6:
 #   print(f"names[2] is going to buy the meal today!")       
#if test_seed == 7 and 8:
 #   print(f"names[3] is going to buy the meal today!")
#if test_seed == 9 and 10:
 #   print(f"names[4] is going to buy the meal today!") 
#else:
 #   print(f"names[5] is going to buy the meal today!")       