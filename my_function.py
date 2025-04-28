#function-A block of reusable code without any function.

def my_function(fname):
    print(fname+"monroe")

my_function("merly")
my_function("livia")

def happy_birthday(name,age):
    print(f"Happy Birthday to you {name}")
    print(f"You are {age} years old")
    print("Happy Birthday to you ")
    print()

happy_birthday("krishna",39)
happy_birthday("Anbu",8)
happy_birthday("Aran",2)

def display_invoice(username,amount,due_date):
    print(f"Hello{username}")
    print(f"your bill of ${amount:.2f}  duedate {due_date}")
display_invoice("Ramya",100.30,"10/6")


