# Lists: ordered, mutable, allows duplicates elements
print("="*7)
print()
# --------------------------------------------------------------

my_list = ["banana", "cherry", "apple",]
print(my_list)

mylist2= [2, True, "Fatima", True, "Fatima", 2]
print(mylist2)


item = my_list[-1] # the last item OR -2 the last second item
print(item)
print()

for fruit in my_list:
    print(fruit)

if "banana" in my_list:
    print("yes")
else:
    print("No")

print(len(my_list))
my_list.append("lemon") # Att the end of the list
print(my_list)
print()

# insert in a specific index
my_list.insert(1, "chai")
print(my_list)
print()

# Remove last item
x = my_list.pop()
print(x, "removed")
print(my_list)
print()

# Remove a specific item
y = my_list.remove("chai")
print(y, "removed")
print(my_list)
print()

# Remove all
# s = my_list.clear()
# print(s)
# print(my_list)
print()


# Reverse
print("="*4, ""*2, "Reverse","="*4, ""*2)
r = my_list.reverse()
print(my_list)
print()

# Sort
print("="*4, ""*2, "Sorted","="*4, ""*2)
s2 = my_list.sort()
print(my_list)

# Trick

print("="*4, ""*2, "Trick","="*4, ""*2)
print()
mylist2 = [0] * 5
print(mylist2) 

# concut
print("="*4, ""*2, "Trick","="*4, ""*2)
print()
new_list = my_list + mylist2
print(new_list)

# slicing // halv part
print("="*4, ""*2, "Slice","="*4, ""*2)
print()
numbers = [1,2,3,4,5,6,7,8]
print("All " , numbers)
print()
halv = numbers[1:5]
print("Sliced ", halv)

# If I have a copy of a list and then I modivied it THIS will modify the original one

# List comperhention
# create a new list of an existense list with one line
print("="*4, ""*2, "List Comperhention","="*4, ""*2)
print()
bNumbers = [1,2,3,4,5,6]
print(bNumbers)

compNumber = [i*i for i in bNumbers]
print("Comperhention the same list:  ",compNumber)





# -------------------------------------------------------------
print()
print("="*7)