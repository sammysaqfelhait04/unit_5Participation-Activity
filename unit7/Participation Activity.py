
print("Welcome to my pizza program!")

print("Type 'quit' when you are done.\n")

active = True 

while active:
    topping = input("Enter a pizza topping: ")
                    
    if topping.strip() == "":
        print("Please enter a valid topping name.")
        continue

    if topping.lower() == "quit":
        active = False
    else:
        print("I will add " + topping + " to your pizza.")

print("\nYour pizza is getting ready!")