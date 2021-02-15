# List and its methods
dish = ["pizza", "MalaiKofta", "Dosa", "Paneer", "Biryani", "Dosa"]

# if duplicate elements then the first occuring element gets deleted
dish.remove("Dosa")
print(dish)

print(type(dish))
print(dish[-1])

dish.append("Samosa")   #add value at the end
print(dish)

dish.insert(1, "Momos")     # Insert at the particular index without replacing the value
print(dish)

# ['pizza', 'Momos', 'MalaiKofta', 'Paneer', 'Biryani', 'Dosa', 'Samosa']
dish[1] = "Pani puri"     # Replace the existing element of that index
print(dish)

dish.remove("Dosa")    # Remove the element with specified value
print(dish)

dish.pop(0)     # Remove elements using index
print(dish)

del dish[0]
print(dish)


# Tuples
vit = ("Bhopal", "Vellore", "Chennai", "AP")
print(type(vit))

# To change tuple value, we can convert it to list - do operations and type cast again to tuple.
vit_list = list(vit)
print(type(vit_list))
print(len(vit)) 


# Sets - {}
vit_campus = {"Bhopal", "Vellore", "Chennai", "AP", "Bhopal"}
print(vit_campus)

# Get individual value of the set
for i in vit_campus:
    print(i)
    if i == 'Vellore':
        print(5)

# Add a value in the set
vit_campus.add("New York")
print(vit_campus)

# Add any other built in data type in the set - like here dish is of list type
vit_campus.update(dish)
print(vit_campus)

# remove() function to remove any value
vit_campus.remove("AP")
print(vit_campus)

# discard() also ignores the specified value and prints rest of the set
# if specified value is not in the set it doesn't give error unlike remove() which gives error
vit.discard("Bhopal")
print(vit)

# deletes the set from memory
del vit_campus
#print(vit_campus)   # Line produces error

# Dictionaries - key:value
mydict = {"10008": "ABC", "100096": "XYZ"}
print(mydict["100096"])

for name in mydict.values():
    print(name)

for key in mydict.keys():
    print(key)

for key, value in mydict.items():
    print(key + ": " + value)
    