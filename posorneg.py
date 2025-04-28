#You are given a number n. The number n can be negative or positive.
#If n is negative, print numbers from n to 0 by adding 1 to n in the neg function.
#If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

def pos(n):
    n-=1
    while n>=0:
        print(n,end=" ")
        n-=1
def neg(n):
    n+=1
    while n <= 0:
       print(n,end=" ")
       n+=1
pos(3)
print()
neg(-3)



