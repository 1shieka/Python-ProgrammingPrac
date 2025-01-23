
def fibonacci(n):
    a, b = 0, 1  
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")  
        a, b = b, a + b  
    print()  

def arithmetic_progression(first, cd, terms):
    print("Arithmetic Progression (AP):")
    current_term = first
    for _ in range(terms):
        print(current_term, end=" ")  
        current_term += cd
    print()  

print("Choose an option:")
print("1. Fibonacci Series")
print("2. Arithmetic Progression (AP)")
choice = int(input("Enter 1 or 2: "))

if choice == 1:
    n = int(input("Enter the number of terms for the Fibonacci series: "))
    fibonacci(n)
elif choice == 2:
    first_term = int(input("Enter the first term of the AP: "))
    common_difference = int(input("Enter the common difference: "))
    terms = int(input("Enter the number of terms: "))
    arithmetic_progression(first, cd, terms)
else:
    print("Invalid choice! Please enter 1 or 2.")

