'''x=str(45)
y=float(45.5)
l1=list(("apple", "banana"))
tup=(x, y)
print(x, y, l1, tup)

dict1=dict(name="John", age=45)
print(dict1)
x1=bytes(5)
print(type(x1))'''

#identity operators
mystring="Hello"
m="hello"
print(m is mystring)
print(m is not mystring)

#if-elif-else
t=20
if t<20:
    print("t is less than 20")
elif t==20:
    print("t is equal to 20")
else:
    print("t is greater than 20")

#for loops
for i in range(0, 50, 2):
    print(i)