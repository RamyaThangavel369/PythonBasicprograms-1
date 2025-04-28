#The number of times 'cat' appears equal the number of times 'hat' appears in the given text?

def cat_hatt(str):
    number_cat=str.count('cat')
    number_hatt=str.count('hat')
    return number_cat==number_hatt
print(cat_hatt("cat hatt cat hatt"))#cat hat cat hat->2cats 2 hats->True
                                #cat hat  hat->1cat 2 hats->False
