'''
sequence[start:stop:step]
'''


#%%
lst = [0, 1, 2, 3, 4, 5]
print(lst[1:4]) 

text= "Python"
print(text[1:4]) 

print(lst[:3])   # Output: [0, 1, 2]
print(lst[3:])   # Output: [3, 4, 5]
print(lst[-4:-1])  # Output: [2, 3, 4]
print(lst[-3:])  # Output: [3, 4, 5]
print(lst[::2])  # Output: [0, 2, 4]
print(lst[1::2]) # Output: [1, 3, 5]
print(lst[::-1])  # Output: [5, 4, 3, 2, 1, 0]
print(text[::-1]) # Output: "nohtyP"
print(lst[1:5:2])  # Output: [1, 3]
print(text[1:5:2]) # Output: "yh"

#slicing entire sequence: Use [:] to create a copy of the sequence.
new_list = lst[:]
print(new_list)  # Output: [0, 1, 2, 3, 4, 5]

print(lst[:100])  # Output: [0, 1, 2, 3, 4, 5]  If stop exceeds the length of the sequence, slicing stops at the end.
print(lst[5:2])  # Output: [] If start is greater than stop, an empty sequence is returned.

#nested slicing
sliced_list = lst[1:5]  # [1, 2, 3, 4]
print(sliced_list[1:3]) # Output: [2, 3]   



#%%
ls = [0, 1, 8, 3, 2, 5]
ls.append(6)
print(ls)

li=ls.sort()
print(li)

print(ls.sort())

ls.sort()
print(ls)

print(sorted(ls))

ls.reverse
print(ls)





