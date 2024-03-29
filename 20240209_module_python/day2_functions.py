import random


def calculate_special_rate(price, maxDiscount, customerRating):
    discount = random.uniform(0.9, 1) * maxDiscount
    specialPrice = price * (1-discount) - (customerRating*price/100)
    return specialPrice


####### PRINT ##########
print("####### CALCULATE SPECIAL RATES ##########")
cust1Price = calculate_special_rate(800, 0.3, 0.9 )
print("Customer 1 Price:", cust1Price)
print("Customer 2 Price:", calculate_special_rate(1230, 0.4, 0.6))


# Write a function in Python (generate_fibonacci) to accept one integer argument (n)
# and generate the Fibonacci series of  n numbers. The series shall start at 1.
# A sample Fibonacci series of 7 numbers: 1, 1, 2, 3, 5, 8, 13
def generate_fibonacci(n):
    next = 1
    count = 1
    previous = 0
    while count <= n:
        print(next)
        current = next
        next += previous
        previous = current
        count += 1


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

generate_fibonacci(10)
print()
print(fibonacci(10))


def fibonacci_iterative(n):
    a, b = 1, 2
    for i in range(n):
        a, b = b, a + b
    return a


n = 7
print("Fibonacci sequence up to", n)
for i in range(n):
    print(fibonacci_iterative(i))


def runFsequence (x, a, f1):
    fn = [f1]
    for i in range(1, x):
        f_next = (fn[i-1]/i+2)*a
        fn.append(f_next)
    print(*fn)

runFsequence(5, 2, 0)

# runFsequence(5,2) ERROR

print('\n\n')
print("####### ARGUMENTS ##################")
print()
def chooseAFruit(*fruits):
    index = random.randint(0,len(fruits)-1)
    print(fruits[index])

chooseAFruit("Apple", "Orange", "Grapes", "Banana")
chooseAFruit("Apple", "Orange", "Grapes", "Banana", "Cherry", "Star")


def chooseAFruit2(name = "Person", *fruits):
    index = random.randint(0,len(fruits)-1)
    print(name, " gets a/an ", fruits[index], sep ="")

chooseAFruit2("Hema", "Apple", "Orange", "Grapes", "Banana")


print('\n\n')
def printAge(age, name = "Person"):
    print(name, "'s age is ", age, sep='')

printAge(56)
printAge(18, 'Fazli')

# function(positional, keyword/default arguments, arbitary arguments)

print('\n\n')
calculate_special_rate2 = lambda price, maxDiscount, customerRating: (
        price * (1-random.uniform(0.9, 1) * maxDiscount) - (customerRating*price/100))
print(calculate_special_rate2(1243, 0.5, 0.9))


print((lambda price, maxDiscount, customerRating: (
        price * (1-random.uniform(0.9, 1) * maxDiscount) - (customerRating*price/100))) (1243, 0.5, 0.9))