import copy


class DataStructureEngine:
    def demonstrateLists(self):
        products = ["hat", "gloves", "shirt", "shirt", "pants", "hat", "shades"]
        marks = [45, 67,88,98,98,100,34]
        isMale = [True, True, False, False, True, True, False]
        itemsInJar =  list(("marble", "marble", "die", 56, 75, 23, True, False))

        print("##### LISTS #####")
        print(products)
        print(marks)
        print(isMale)
        print(itemsInJar)

        print("Products:", products)

        print("\n\n")
        print(len(products)) # The Count of List Items
        print(type(products)) # The Type of the List

        print("\n\n")
        print(products)
        print(products[5]) # Indexes start with 0. The 6th Item is retrieved.
        print(products[-1]) # The last item
        print(products[:3]) # [0,3)
        print(products[3:])  # [3,last item]
        print(products[-4:-1])  # [-4, -1)

        # [START : STOP : STEP]
        print("\n\n")
        print(products)
        print(products[ : : -1])
        str1 = "It is such a dull day!!"
        print(str1)
        print(list(str1))
        print(products)
        print(products[:: 2]) # Start to End, Skip 1 Item.
        print(products[:3: -1])  # If it is a - step, start and stop will be switched.
                                # (stop, start]
        print(products[5:3: -1])  # If it is a - step, start and stop will be switched.
        # (stop, start]
        print(products[5:1: -2])

        print("\n\n")
        print(products)
        products[3] = "jacket"
        print(products)
        products[3] = ["jacket","hat"]
        print(products)
        products[3:4] = ["jacket","hat"]
        print(products)
        products[3:4] = ["jacket", "hat", "scarf"]
        print(products)
        products[3:5] = ["shoes"]
        print(products)
        products[3:5] = "shoes"
        print(products)
        products[3:8] = ["shoes"]
        print(products)

        print("\n\n")
        # List Methods
        print(products)
        products.append("ring")
        print(products)
        products.insert(2, "ring")
        print(products)
        prod2 = ["scarf","gloves","shorts"]
        products.extend(prod2)
        print(products)

        print("\n\n")
        products2 = products
        print(products)
        print(products2)

        products2.pop(2)
        print(products)
        print(products2)

        products3 = products.copy()
        products3.pop()
        print(products)
        print(products3)

        # copy.deepcopy(products3) - Create a hard/deep copy of the object in the memory

        print(products)
        products.sort()
        print(products)
        products.sort(reverse=True)
        print(products)

        print(marks)
        marks.reverse()
        print(marks)

    def doEx1(self):
        # We have a list, which is called fruits. And the fruits has the following values: Fruits = [‘Apple’, ‘Banana’, ‘Kiwi’]
        # We want to the reversed order fruits. But please don’t modify the original list.
        # Please update the original fruits list in memory.
        #
        # Add new item to list after a specified item. Write a program to add item 7000 after 6000 in the following Python List.
        #         list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

        fruits = ['Apple', 'Banana', 'Kiwi']
        fruits_r = fruits.copy()
        fruits_r.reverse()
        print(fruits)
        print(fruits_r)

        list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
        print(list1.index(20))
        print(list1)
        list1[2][2].append(7000)
        print(list1)

        list2 = [4,4,4,5,6,7,7,3,4,2]
        print(list2.index(4))

    def demonstrateTuples(self):
        studentRecord1 = ('Nabeel', 24, '6453124221', 1, 'moderate')
        studentRecord2 = tuple(('Fazli', 35, '6463232422', 4, 'strong'))

        print(studentRecord1)
        print(studentRecord2)

        # Subsetting is similar to lists
        print(studentRecord2[2])

        # studentRecord2[2] = '2443253532' - Error
        print(studentRecord2.index(35)) # If the value is not found, an Error is fired.
        print(studentRecord2.count(24))

        studentRecord1_l = list(studentRecord1)
        studentRecord1_l[2] = '2443253532'
        studentRecord1 = tuple(studentRecord1_l)
        print(studentRecord1)

        print('\n\n')
        print(studentRecord1)
        (name, age, phone, spouses, status) = studentRecord1
        print(age)
        print(phone)

        print('\n\n')
        print(studentRecord2)
        (name, age, phone, *otherInfo) = studentRecord1
        print(age)
        print(phone)
        print(otherInfo)

        a, b = 56, 87
        print(a, b)



dse = DataStructureEngine()
#dse.demonstrateLists()
#dse.doEx1()
dse.demonstrateTuples()