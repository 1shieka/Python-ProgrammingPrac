#%%
mylist = ['Hi', 'Im', 'Cherry']
print(mylist[2])

# %%
# Input Integer List
list1 = input("Enter a list of integers: ")
list2 = list(map(int, list1.split()))

# Reversing the list
reversed_list = list2[::-1]  #Using slicing
print("Reversed List:", reversed_list)

# Finding frequencies
list2 = list(map(int, list1.split()))  
frequency_d = {}
for num in list2:
    if num in frequency_d:
        frequency_d[num] += 1  
    else:
        frequency_d[num] = 1  

print("\nFrequency of each integer:")
for key, value in sorted(frequency_d.items()):
    print(f"{key}: {value} times")


# Checking if the list is an anagram
list3 = input("Enter another list of integers separated by spaces: ")
list4 = list(map(int, list3.split()))
if sorted(list2) == sorted(list4):  # Compare sorted lists
    print("Lists are anagrams.")
else:
    print("Lists are not anagrams.")

