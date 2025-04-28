#Iterable-An object/collection that can return its elements one at a time.
#python can go through each character one by one.__iter__()
#set,tuples,Dictionaries,List,string-iterable.

#SET:

fruits = {"Apples", "Banana", "Cherry", "Guava", "Grapes"}

for fruit in fruits:
    print(fruit)

#LIST

numbers=[1,2,3,4,5]
for number in numbers: #Every number in iterable
    print(number,end=" ")

#Tuples
numbers=(1,2,3,4,5)
for number in numbers: #Every number in iterable
   print(number)

 #Dictionary
my_dictionary={"A":"2","B":"3","C":4}
for keys,values in my_dictionary.items():
  print(f"{keys}:{values}")

 #STRING
Name="Ramya Thangevel"
for k in Name:
 print(k,end="")
"""
nums=[1,2,3,4]
it=iter(nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())"""
