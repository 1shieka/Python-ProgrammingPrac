#%%
tuple1 = (1, 2, 3, 4) # tuple formation
print(tuple1)

tuple2 = (1, "Hello", 3.5) # tuple with multiple data types
print(tuple2)

tuple3 = (5,) # A tuple with a single element (note the comma)
print(tuple3)

tuple4 = () #empty tuple


#%%

tuple1 = (10, 20, 30, 40)  # Access by index
print(tuple1[0])  # Output: 10
print(tuple1[-1])  # Output: 40

tuple1 = (1, 2, 3, 4, 5, 6) # Tuple slicing
print(tuple1[1:4])  # Output: (2, 3, 4)
print(tuple1[:3])   # Output: (1, 2, 3)
print(tuple1[3:])   # Output: (4, 5, 6)

result = tuple1 + tuple2 # Concatenation
print(result)  

tuple3 = ("a", "b") # Repetition
result = tuple3 * 3
print(result)  # Output: ('a', 'b', 'a', 'b', 'a', 'b')

print(len(tuple1)) # Length of a tuple
