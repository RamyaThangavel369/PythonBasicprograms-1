#set:Collection which is unordered,unchangeable,unindexed.No duplicate values.
#The output come in the unordered list.count

utensils={"fork","Knife","spoon"}
dishes={"bowl","plate","Cup"}
utensils.add("Napkins")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)
dishes.update(utensils)
dinner_table=utensils.union(dishes)
dinner_table=dishes.difference(utensils)
dinner_table=utensils.intersection(dishes)
for a in utensils:
    print(a)
for a in dishes:
    print(a)
for a in dinner_table:
    print(a)
