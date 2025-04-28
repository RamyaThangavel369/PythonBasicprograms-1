#swap the first and last element of the list using Python
def my_list():
    my_list=[1,2,3,4,5]
    my_list[0],my_list[-1]=my_list[-1],my_list[0]
    print("Swap the first and last elements:",my_list)
my_list()