
import random
import random as rn
from random import uniform as runif

print(5 * 30)
print("Hello, Matilda!!!")

print()
print("###########")
no_students = 50
print('The class has', no_students, 'students')
if no_students >= 25:
    print('That is a large class.')
    print('The prof will be tired.')
else:
    print('That is a small class.')

print("###########")
print()
print("########### DATA TYPES #######")
x = "Hello World"
print("1.",x,":", type(x))

x = 20
print("2.",x,":", type(x))

x = 20.5
print("3.",x,":", type(x))

x = 1j
print("4.",x,":", type(x))

x = ["apple", "banana", "cherry"]
print("5.",x,":", type(x))

x = ("apple", "banana", "cherry")
print("6.",x,":", type(x))

x = range(6)
print("7.",x,":", type(x))

x = {"name" : "John", "age" : 36}
print("8.",x,":", type(x))

x = {"apple", "banana", "cherry"}
print("9.",x,":", type(x))

x = frozenset({"apple", "banana", "cherry"})
print("10.",x,":", type(x))

x = True
print("11.",x,":", type(x))

x = b"Hello"
print("12.",x,":", type(x))

x = bytearray(5)
print("13.",x,":", type(x))

x = memoryview(bytes(5))
print("14.",x,":", type(x))

x = None
print("15.",x,":", type(x))

print("###########")
print()
y = str(65)
print("1.",y,":", type(y))
y = int("65")
print("2.",y,":", type(y))
# y = int("65.5")
# print("3.",y,":", type(y))
y = float("65.54")
print("3.",y,":", type(y))
y = int(65.54)
print("4.",y,":", type(y))

y = bool(65.54)
print("5.",y,":", type(y))
y = bool("65.54")
print("6.",y,":", type(y))
y = bool(-4)
print("7.",y,":", type(y))
y = bool(0)
print("8.",y,":", type(y))
y = bool("0")
print("8.",y,":", type(y))
print(True)
print(False)


print("###########")
print()
print("########### STRINGS #######")

str1 = 'This is a great class!!!'
str2 = "J's favourite animal is rat"

str3 = """Lists (known as arrays in other languages) are one of the compound 
data types that Python understands. Lists can be indexed, 
sliced and manipulated with other built-in"""

print(str1)
print(str2)
print(str3)
print()
print(len(str3))

print("sliced" in str3)
print("world" in str3)
print("world" not in str3)
print()

str4 = "Today is a fine day!!!"
print(str4)
print(str4[2])
print(str4[6:8])    # substring [6, 8)
print(str4[:5])    # substring [0,5)
print(str4[10:])    # substring [10,endIndex]

str5 = "Good Day"
print(str5[3])
print(str5[-5])

print(str5[3:-1])
print(str5[-5:-1])
print(str5[ : :-1])

print()
print("########### OPERATORS #######")
print(1+2)
print(1-2)
print(2*643.4)
print(2**256)
print(56//4)
print(56%4)

x = 45
# x = x + 5
x += 5

# x = x * 8
x *= 8

y = random.uniform(10,50)
z = random.normalvariate(10,50)
print(y)
print(z)

if y >= z or z < 0:
    print("I am going crazy!!!!!@!#@$@%@")
else:
    print("I am not THAT crazy.")

if type(y) is int:
    print("y is INT")
else:
    print("y is NOT INT")

print(type(y))
if type(y) is float:
    print("y is FLOAT")
else:
    print("y is NOT FLOAT")

print(4 > 8 and 8 < 9)
print(4 & 6)

"""

100
110
----
100
"""

print(random.normalvariate(76, 32))
print(rn.normalvariate(76, 32))
print(rn.normalvariate(76, 32))
print(runif(76, 32))