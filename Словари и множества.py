my_dict = {"Sara" : 1992, "Jack" : 1998, "Schnebjolock" : 2000}
print(my_dict)
print(my_dict["Sara"])
my_dict["Andrej"] = 2002
print(my_dict["Andrej"])
my_dict.update({"Igor" : 2001,
                "Inokentij" : 1996})
del my_dict["Sara"]
print(my_dict.get("Sara"))
print(my_dict)
my_set = {1,2,2,1,True,False,"Ingvar",1.1,1.1}
print(my_set)
my_set.add("5")
my_set.add("Stiven")
my_set.discard("5")
print(my_set)