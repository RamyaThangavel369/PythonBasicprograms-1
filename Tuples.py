#Tuples:Collection which is ordered,unchangeable,no duplicate value allow.

student=("Ramya",34,"Female")
print(student)
print(student.count("Ramya"))
print(student.index("Female"))
for n in student:
    print(n)
if "Ramya" in student:
    print("Ramya is here!")


