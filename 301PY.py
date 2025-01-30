#%%
#Count and display the number of capital letters in a given string 

text = input("Enter a string: ")
count=0
caps=""
for char in text:
    if char.isupper():
        count += 1  
        caps += char + " "

print("Total number of capital letters: ", count)
print("Capital letters found: ",caps)


#%%
#Count total number of vowels in a given sentence and also give the frequency
text = input("Enter a string: ")

count = 0
letters = ""  
vowels = "AEIOUaeiou"
frequency = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for char in text:
    if char in vowels:
        count += 1  
        letters += char + " "  
        frequency[char.lower()] += 1  

print("\nTotal number of vowels:", count)
print("Vowels found:", letters)

print("\nFrequency of each vowel:")
for vowel, freq in frequency.items():
    print(vowel, ":" ,freq)
            


#%%
#Input a sentence and print words in separate lines

text = input("Enter a sentence: ")
words = text.split()

print("Words in the sentence entered:")
for word in words:
    print(word)

#%%
#Enter a string and substring. You have to print the number of times that the substring occurs in a given string.
#String traversal will take place from left to right and not from right to left.
#Sample input : ABCDCDC


main= "ABCDCDC"
substring = "BC"
occurr = main.count(substring)

print(substring,"occurs",occurr,"times.")

# %%
