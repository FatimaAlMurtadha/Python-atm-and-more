# Dictionary: key-Value pairs, Unordered, mutable

print("="*50)
print()
# --------------------------------------------------------------

mydiction = {"name": "Fatima", "age": 32, "city": "Malmö"}

print(mydiction)

# new dic w/o quates
mydiction2 = dict(name="Ahmed", age= 40, city="Malmö")

print()
print("="*4, ""*2, " New dic  ","="*4, ""*2)
print()
print(mydiction2)

# Access with a value 
value = mydiction2["age"]
print(value)
print()

mydiction.popitem()
print("items now: ", mydiction)










print("="*50)
print()
# --------------------------------------------------------------