'''
Arithmetic Operator (Mathematical) (Modulus operator)
Relational Operator (comparison operator == >< =! etc ) Result is either true or false (Boolean)
Logical Operator (and or not) (for combination)
Assignment Operator (= += -=) (a+=b == a=a+b)
Comparison operator (if else)
'''
#Modulus function and negative integar logic  6*3 = 18 and -16 so 18-16=2
a = -16 % 6  
b = 16 % -6  
c = -16 % -6  
d = 16 % 6  
print("-16 % 6 =",a)
print("16 % -6 =",b)
print("-16 % -6 =",c)
print("16 % 6 ",d)

Num1= int(input("Enter Number1:"))
Num2= int(input("Enter Number2:"))
a= Num1>Num2 
b= Num1<Num2
c= Num1==Num2
print("\nResults:", end="")
print(Num1,">",Num2,"=",a)
print(Num1,"<",Num2,"=",b)
print(Num1,"==",Num2,"=",c)
