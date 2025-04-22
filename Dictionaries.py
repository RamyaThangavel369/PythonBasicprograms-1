#Dictionaries-a collections of {key:value} pairs.ordered,changeable.No duplicate values

capitals={"USA":"WASHINGTON D.C","INDIA":"NEW DELHI","CHINA":"BEIJING","RUSSIA":"MOSCOW"}
#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("RUSSIA"))
#if capitals.get("INDIA"):
 #   print("The capital exist")
#else:
 #   print("The capital doesn't exist")
#capitals.update({"GERMANY":"BERLIN"})
#print(capitals)
#capitals.pop("china")
#capitals.update({"USA":"CALIFORNIA"})
#capitals.clear()
#keys=capitals.keys()
#for key in capitals.keys():
  #  print(keys)
#values=capitals.values()
#for value in capitals.values():
    #print(values)
#items=capitals.items()
#for item in capitals.items():
    #print(items)
for key,value in capitals.items():
  print(f"{key}:{value}")
