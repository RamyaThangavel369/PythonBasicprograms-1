
#Array:Arrays are used to store multiple values in one single variable
def Arrays_list():
    list1=[8,2,4,5,7]
    list2=[1,6,8,9,3]
    list3=[3,8,9,4,3]
    for i in list1:
     for k in list2:
      for m in list3:
          if i==k==m:
              print(k)
Arrays_list()

#write the program to find the sum of elements in a list?
"""
def Arrays_list():
    list=[23,56,74,43,21]
    sum=0
    for i in list:
          sum=sum+i
    print("Sum of list is",sum)
Arrays_list()"""

#Program to find the minimum and maximum element of array?
arr=[21,10,56,43,24]
print("min",min(arr))
print("max",max(arr))
minimum=arr[0]
for i in range (len(arr)):
    if arr[i]<minimum:
         minimum=arr[i]
print(minimum)
maximum=arr[0]
for i in range (len(arr)):
    if arr[i]>maximum:
         maximum=arr[i]
print(maximum)







