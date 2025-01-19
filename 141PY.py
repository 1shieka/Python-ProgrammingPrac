#string length 

a = "Hello"
ab= len(a)

b = "hello hi"
print(ab)
print(len(b))

#concatenation 

a = "Hello"
b = "World"
c = a + b
print(c)

a0 = "Hello "
b0 = "World"
c0 = a0 + b0
print(c0)

a1= "2"
b1= "3"
c1= a1+b1
print(c1)

a2= 2
b2= 3
c2= a2+b2
print(c2)

#array indexing starts from 0 because there's no offset caclulation 

a = "Hello"
print(a[0])
print(a[3])
print(a[4])


#slicing 

e = "Hello  World!"
print(e[2:5])


#endswith : Value in true and false 

text= "hello I'm Pikaa"

x = text.endswith("Pikaa")

print(x)

#startswith : Value in true snd false 

y = text.startswith("Hello")
print(y)

#capitalize 

z = text.capitalize()
print(z)

#replace 

f = text.replace("Pikaa" , "Avii")
print(f)
print(text)

#count : substring count 

g = text.count("a")
h = text.count("A")
print(g,h)


text = text.replace("Pikaa" , "Avii")
print(text)


g = text.count("a")
h = text.count("A")
print(g,h)  