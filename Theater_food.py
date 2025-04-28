print("WELCOME TO THE THEATER")
menu={"Pizza":8.00,"Burger":5.00,"Chips":10.00,"Nachos":7.00,"Cheese pasta":6.00,"French fries":2.00,"Icecream":3.00,"Juices":4.00}
cart=[]
total=0
print("Menu of the special day")
print("-----------------------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("-----------------------")
while True:
    food=input("Select an item(q to quit):").lower()
    if food=="q":
        break
    elif menu.get(food)is not None:
        cart.append(food)
print("----YOUR Order---")
for food in cart:
    total+=menu.get(food)
    print(food,end="")

print()
print(f"Total is:${total:.2f}")


