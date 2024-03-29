import random
import string


class ControlStructureEngine2:
    def demonstrateForLoop(self):
        ages = [56, 74, 18, 25, 67, 43]
        count = 1

        for age in ages:
            print("Person", count, "age: ", age)
            count += 1

        print()
        for i in range(len(ages)):
            print("Person", i+1, "age: ", ages[i])

        print()
        myName = "Maddy Nana"
        counter = 1
        for x in myName:
            print(x + ":", counter)
            counter += 1

        print()
        newName = "Chris Evans"
        newName_i = iter(newName)
        print(next(newName_i))
        print(next(newName_i))
        print(next(newName_i))

        print()
        count = 0
        for age in ages:
            count += 1
            if age % 2 == 1: continue
            if age % 5 == 0: break
            print("Person", count, "age: ", age)

        print()
        for age in ages:
            print("There is a person of the age", age)
        else:
            print("All data points successfully scanned.")

        print()
        for age in ages:
            print("There is a person of the age", age)
            if age % 2 == 0: break
        else:
            print("All data points successfully scanned.")

    def demonstrateRange(self):
        multis3 = range(3, 50, 3)
        print(multis3)
        print(list(multis3))

    def demonstrateListComprehension(self):
        # generate 10 random integers from the range 10 - 100 and place them
        # in a list.
        list = []
        for i in range(10):
            list.append(random.randint(10,100))

        # [ <calculation/expression on var> for var in iterable <condition>]
        num_list = [ random.randint(10,100) for _ in range(10)]
        print(num_list)

        # use num_list. If each number is an even number, generate a random LETTER.
        # Collect them into a list.
        print()
        print(string.ascii_uppercase)
        letter_list = [ string.ascii_uppercase[random.randint(0,25)]
                        for num in num_list if num % 2 == 0]
        print(letter_list)

        # Set comprehension
        letter_list = {string.ascii_uppercase[random.randint(0, 25)]
                       for num in num_list if num % 2 == 0}
        print(letter_list)

        #Dict comprehension
        #[ key_expression : value_expression for var in iterable <condition>]
        people = ["Andy", "Emmanuel", "Hema", "Saranya", "Fazli"]
        people_age = { name : random.randint(18, 60) for name in people}
        print()
        print(people_age)

    def demonstrateWhile(self):
        num_list = [random.randint(10, 100) for _ in range(10)]

        cumlt_total = 0
        index = 0
        print(num_list)
        while cumlt_total <= 50:
            cumlt_total += num_list[index]
            startIndex = random.randint(0, 25);
            token = string.ascii_uppercase[startIndex:startIndex+3]
            print(token)
            index += 1

    def demonstrateMatchCase(self):
        status = random.randint(1,5)*10
        print(status)

        match status:
            case 10:
                print("File Active!")
            case 20:
                print("File Deleted")
            case 30:
                print("File Updated")
            case 40:
                print("File renamed")
            case 50:
                print("File Corrupt")

        match status:
            case 10:
                print("File Active!")
            case 20 | 50:
                print("File is not Available")
            case 30:
                print("File Updated")
            case 40:
                print("File renamed")
            case _:
                print("Unsupported Status Message")

        print()
        num_list = [random.randint(10, 100) for _ in range(10)]
        print(num_list)
        num_list2 = [x for x in num_list if x % 2 == 0]

        match num_list2:
            case [a]:
                print("Not a good match:", [a])
            case [a, b]:
                print("A match with two numbers:", [a, b])
            case[a, b, c]:
                print("A match with three numbers:", [a, b, c])
            case [a, b, c , *rest]:
                print("Multiple Matches:", [a, b, c, *rest], ". a is ", a, " and the rest is", rest)

        print()
        # match-case guarded with if.
        student = {'name': 'Kate', 'grade': 90, 'courses': 16}
        match student:
            case {'name': name, 'courses': courses, 'grade': grade} if courses > 15 and grade >= 90:
                print(name, "is Exceptional")
            case {'name': name, 'courses': courses, 'grade': grade} if grade >= 90:
                print(name, "Good")
            case _:
                print(name, "No current award")

        print()
        num1 = 45
        match num1:
            case a if a > 50:
                print("Well done!")
            case a if a > 30:
                print("Good!")
            case _:
                print("Try to improve")

    def doEx1(self):
        # A: Given a positive integer list, that is called "numbers“, e.g.
        # numbers = [10, 2, 4, 1, 6, 18], what are the two values,
        # whose sum becomes the maximum in the list? (Please write the
        # function that returns the two values.)
        numbers = [random.randint(1, 100) for _ in range(random.randint(2,30))]
        print("Two Max Numbers:",self.extractTwoValuesWithHighestTotal(numbers))


        #B: Generate a list of random integer numbers, with 20 numbers.
        # Find the sum of all even numbers and odd numbers separately
        # from the generated list using a for loop. Assign the values to
        # two variables and print them.
        print()
        totals = { "odd_totals": 0, "even_totals": 0}
        numbers = [random.randint(1, 100) for _ in range(20)]
        for num in numbers:
            if num % 2 == 0: totals["even_totals"] += num
            else: totals["odd_totals"] += num

        print(totals)

    def extractTwoValuesWithHighestTotal(self, num_list):
        num_list.sort(reverse=True)
        return num_list[:2]


cse2 = ControlStructureEngine2()
# cse2.demonstrateForLoop()
# cse2.demonstrateRange()
# cse2.demonstrateListComprehension()
# cse2.demonstrateWhile()
# cse2.demonstrateMatchCase()
cse2.doEx1()