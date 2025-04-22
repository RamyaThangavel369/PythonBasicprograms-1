#Lambda-A small anonymous function for onetime use(throw away function).
      # They take anynumber of arguments,but have only 1
       # 'sort()','map()','filter()','reduce()'

  # lambda parameters: expression
"""
double=lambda x: x*2
print(double(5))
add=lambda x,y:x+y
print(add(3,5))
max_value=lambda x,y:x if x>y else y
print(max_value(2,3))
min_value=lambda x,y:x if x<y else y
print(min_value(6,3))
name=lambda firstname,lastname:firstname+" "+lastname
print(name("Ramya"," Thangavel"))
is_even=lambda x:x%2 == 0
print(is_even(4))
is_odd=lambda x:x%2 ==0
print(is_odd(5))
age_check=lambda age:True if age>=18 else False
print(age_check(20))"""

#map:
#map(function,condition)
"""
def c_to_f(temp):
    return (temp*9/5)+32
celsius_temp=[0.0,10.0,20.0,30.0]
fahrenheit_temp=map(c_to_f,celsius_temp)
for temp in fahrenheit_temp:
    print(temp)
#print(celsius_temp)"""

#list:
"""
def c_to_f(temp):
    return (temp*9/5)+32
celsius_temp=[0.0,10.0,20.0,30.0]
fahrenheit_temp=list(map(c_to_f,celsius_temp))
#for temp in fahrenheit_temp:
print(fahrenheit_temp)
#print(celsius_temp)"""

celsius_temp=[0.0,10.0,20.0,30.0]
fahrenheit_temp=list(map(lambda temp:(temp*9/5)+32,celsius_temp))
print(fahrenheit_temp)
