#%%
#Traffic Light 
light = input("Enter Light: ").strip().capitalize()
if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Wait")
elif light == "Green":
    print("Go")
else:
    print("Wrong Input")

#%%
#Driving Licence and Voting Eligibility
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You can Drive")
    print("You can Vote")
else:
    print("You're not Eligible to Drive and Vote ")

#%%
#Grading System 
marks= int(input("Enter Marks"))
if marks==100:
    print("Perfect")
elif marks >= 90:
    print("Outstanding")
elif marks >= 75:
    print("Good")
elif marks >= 55:
    print("Average")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


#%%
#3 inputs and maximum number 
a= int(input("Enter Number1: "))
b= int(input("Enter Number2: "))
c= int(input("Enter Number3: "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print("The maximum number is:", maximum)



#%%
#Multipe, of 7
mul= int(input("Number:"))
if mul%7==0:
    print("It's Divisible")
else:
    print("It's not divisible")
    


