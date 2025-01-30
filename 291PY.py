#%%
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial not defined .")
elif num == 0 or num == 1:
    print("The factorial of",num,"is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of",num,"is",factorial)



#%%
i = 1
while i <= 5:
    print(" " * ((5 - i) // 2) + "*" * i)
    i += 2
    
i = 3
while i > 0:
    print(" " * ((5 - i) // 2) + "*" * i)
    i -= 2