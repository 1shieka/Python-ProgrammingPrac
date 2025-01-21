# %%
#Check if a number in a list in a palindrome
list2 = input("Enter a list of integers separated by spaces: ")
reversed = list2[::-1]  # Reverse the list
if list2 == reversed:  
    print(list2, "equals to", reversed, ": List is a palindrome.")
else:
    print(list2, "not equal to", reversed, ": List is not a palindrome.")


# %%
#check if the list is an armstrong number 
x = int(input("Enter a number: "))
temp=x
power = len(str(x)) #convert to string because len is only for string 
sum=0
while x > 0:
    digit= x%10
    sum=sum+digit**power  #or sum+=digit**power
    x= x//10 #or x//=10

if (temp==sum):
    print("Armstrong Number")
else:
    print("Not An Armstrong Number")


# %%
#print the list of armstrong number upto a given number
lower = int(input("Enter the lower limit"))
upper = int(input("Enter the upper limit"))
print("List of armstrong numbers between", lower ,"and",upper)
for num in range(lower, upper + 1):
   power = len(str(num))
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** power
       temp //= 10

   if num == sum:
       print(num)
