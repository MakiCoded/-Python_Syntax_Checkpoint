# Welcome Message

print("Welcome to Python Pizza Deliveries")

# select pizza size
size = input("What size of Pizza do you want? (small/medium/large) \n").lower()
# select add peperoni 
add_Peperoni = input("Would you want to add Peperoni? (yes/no) \n").lower()
# select add Extra Cheese
add_extraCheese = input("would you want extra Cheese? (yes/no) \n").lower()

# initializing Base price
final_Price = 0

# Calculating the base price based on the size of the pizza
if size == "small":
    final_Price += 15
elif size == "medium":
    final_Price += 20
elif size == "large":
    final_Price += 25
else:
    print("Invalid size entered!")

# Adding the cost of pepperoni
if add_Peperoni == "yes":
    if size == "small":
        final_Price +=2
    elif size in ["medium", "large"]:
        final_Price +=3

# Adding the cost of extra cheese
if add_extraCheese == "yes":
    final_Price += 1

# Displaying the final price
print(f"Your final bill is: ${final_Price}")




