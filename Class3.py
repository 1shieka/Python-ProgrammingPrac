#%%
a = input("Enter a word: ").strip()

#Index Printing 
ind=0
while ind < len(a):
    print("Index[", ind, "] : " , a[ind])
    ind += 1

#%%
#Odd Even
b = int(input("Enter a number: "))
if b%2==0 :
    print("Number is EVEN")
elif b%2!=0:
    print("Number is ODD")
else:
    print("Error")

#%%
#Prime Number
# Itersate from 2 to b//2
# If num is divisible by any number between
# 2 and n / 2, it is not prime
if b > 1:
  
    for i in range(2, (b//2)+1):
        
        if (b % i) == 0:
            print(b, "is not a prime number")
            break
    else:
        print(b, "is a prime number")
else:
    print(b, "is not a prime number")