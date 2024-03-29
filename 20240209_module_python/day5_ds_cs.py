import random


class DataStuctureEngine2:
    def doTupleEx(self):
        # We have a list of tuples that contain the information of some employees.
        #     employee_details = [(1, "AA", 100),(1, "BB", 1001),(1, "cc", 1002)]
        # How would you access the details of 2nd employee?
        # How would you print the name of the second employee?
        #
        #
        # Consider:
        #         student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
        # If student_id keys were to be stored separately, what would be the most suitable data structure and why?
        employee_details = [(1, "AA", 100), (1, "BB", 1001), (1, "cc", 1002)]
        print(employee_details)
        print(employee_details[1])
        print(employee_details[1][1])

        print()
        student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
        idKeys = tuple(student_id.keys())
        print(idKeys)  # A tuple is more suitable as the values are ordered (indexed) and would be "immutable".

    def demonstrateSets(self):
        student_ids = {1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9}
        print()
        print("###### SETS ######")
        print("Student_IDs:", student_ids)
        student_ids.add(10)
        student_ids.add(9)
        print("Student_IDs:", student_ids)

        student_ids2 = {11, 12, 13, 14, 1, 2, 3}
        student_ids.update(student_ids2)
        print("Student_IDs:", student_ids)

        print()
        print(type(student_ids2))

        print()
        print("Student_IDs:", student_ids)
        student_ids.pop()  # Delete a random item
        print("Student_IDs:", student_ids)
        student_ids.pop()
        print("Student_IDs:", student_ids)
        student_ids.remove(10)
        print("Student_IDs:", student_ids)

        student_ids2.clear()
        print("Student_IDs - 2:", student_ids2)

        print()
        for x in student_ids:
            if x == 14:
                print("ID 14 is FOUND!!")

        print()
        event1 = {'CAN', 'NIG', 'PAK', 'LKA', 'FRA', 'SAU', 'JAM', 'IND', 'USA', 'GBR', 'ESP'}
        event2 = {'CAN', 'NIG', 'PAK', 'GBR', 'ESP', 'ARG', 'MEX', 'JPN', 'ARE', 'COL', 'DOM', 'BRA'}

        print("Event 1 Attendees:", event1)
        print("Event 2 Attendees:", event2)

        event1_c = event1.copy()
        event2_c = event2.copy()

        # Countries attended ANY of the 2 events
        any_event = event1.union(event2)
        print("Countries attended ANY of the 2 events:", any_event)
        event1_c.update(event2_c)  # Directly updates event1_c

        # Countries attended BOTH events
        both_events = event1.intersection(event2)
        print("Countries attended BOTH events:", both_events)
        event1_c = event1.copy()
        event2_c = event2.copy()
        event1_c.intersection_update(event2_c)  # Directly updates event1_c

        # Countries attended event 1 ONLY
        event1_only = event1.difference(event2)
        print("Countries attended event 1 ONLY:", event1_only)
        event1_c = event1.copy()
        event2_c = event2.copy()
        event1_c.difference_update(event2_c)  # Directly updates event1_c

        # Countries attended ONLY ONE event
        one_event = event1.symmetric_difference(event2)
        print("Countries attended ONLY ONE event:", one_event)
        event1_c = event1.copy()
        event2_c = event2.copy()
        event1_c.symmetric_difference_update(event2_c)  # Directly updates event1_c

    def run_sets_question(self):
        countries = {'Brazil', 'USA', 'Canada', 'Colombia', 'Mexico', 'England'}
        countries.remove('USA')

        """ 
        exc_countries = {'USA'}
        countries.difference_update(exc_countries)
        """

        event1 = {'I0001', 'I0011', 'I0012', 'I0013', 'I0016', 'I0301', 'I0221', 'I2301'}
        event2 = {'I0001', 'I0009', 'I1012', 'I0013', 'I0016', 'I0501', 'I4221', 'I2341'}

        print(event1)
        print(event2)
        event1.remove('I0221')

        print(event1)
        print(event1.intersection(event2))

    def demonstrateDicts(self):
        doc1 = {'name': "assignment1",
                'ext': 'docx',
                'size': 80,
                'encrypted': True}

        print('#### DICTS ####')
        print('Document 1:', doc1)
        print('Document 1 Name:',doc1['name'])

        doc1['name'] = 'assignment2'
        print('Document 1 Name:', doc1['name'])

        doc1['path'] = 'D:\\TSoM'
        print('Document 1:', doc1)

        doc1.update({'name': "assignment1",
                'desc': 'This is the final assignment file'})
        print('Document 1:', doc1)

        print(type(doc1))

        print()
        print(doc1.items())
        print(type(doc1.items())) # dict_items

        print(list(doc1.items())[1][0]) # the key of the second key-value pair
        print(doc1.keys())
        print(type(doc1.keys())) # dict_keys
        print(doc1.values())
        print(type(doc1.values())) # dict_values

        print()
        doc1.pop('desc')
        print(doc1)

        print(doc1.get('name'))

        doc2 = dict(name =  "assignment1",
                ext = 'docx',
                size = 80,
                encrypted = True)

        print(doc2)

    def run_dict_question(self):
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "Max speed": 150,
            "year": 1964,
            "Made in": "USA"
        }

        print(car["brand"])

        """
        A company wants to save their customer's sign up information in dictionaries , 
        you are asked to perform the following task :
        create a template dictionary, with the following keys: 
            first name, last name, e - mail, password.
        create a function  that accepts four arguments and returns a new dictionary for a new customer.
        """
        print()
        customer1 = Customer('James', 'Potter', 'j_potter@gmail.com', 'yts@$$sad2')
        print(customer1.generate_customer_dict())

        print()
        person = {'name': 'Salam', 'age': 44, 'city': 'Niagara', 'height': 164}

        person.pop('age')
        print(person)




class Customer:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    __customer_dict__ = {'first_name' : str(),
                    'last_name' : str(),
                    'email': str(),
                    'password' : str()}

    def generate_customer_dict(self):
        self.__customer_dict__['first_name'] = self.first_name
        self.__customer_dict__['last_name'] = self.last_name
        self.__customer_dict__['email'] = self.email
        self.__customer_dict__['password'] = self.password

        return self.__customer_dict__


class ControlStructureEngine:
    def demonstrateIf(self):
        age = int(random.uniform(18, 80))

        print('#### if..elif...else ####')
        if age >= 50:
            print('AGE:',age,' -- GROUP A')
        elif age >= 30:
            print('AGE:',age,' -- GROUP B')
        else:
            print('AGE:',age,' -- GROUP C')

        salary = random.randint(1000, 10000)

        if age >= 50 and salary >= 5000:
            print('AGE:',age, '| SALARY:',salary, ' -- GROUP XX')
        elif age < 50 and salary >= 5000:
            print('AGE:',age, '| SALARY:',salary, ' -- GROUP YY')
        elif age >= 50 and salary < 5000:
            print('AGE:', age, '| SALARY:', salary, ' -- GROUP ZZ')
        else:
            print('AGE:', age, '| SALARY:', salary, ' -- GROUP XYZ')

        if age > 50: print('LEVEL 1 EMP!!!')
        if age > 50: salary += 500

        print('AGE:', age, '| SALARY:', salary)

        print()
        print('LEVEL 1 EMP!!!') if age > 50 else print('LEVEL 2 EMP!!!')

        print()
        print('LEVEL 1 EMP!!! SALARY:', (lambda x: x+500)(salary)) if age > 50 else print('LEVEL 2 EMP!!! SALARY:',salary)

        print()
        print('LEVEL 1 EMP!!!') if age > 50 else print('LEVEL 2 EMP!!!') if age > 30 else print('LEVEL 3 EMP!!!')




###### EXECUTION OF THE CODE ########
dse2 = DataStuctureEngine2()
# dse2.doTupleEx()
# dse2.demonstrateSets()
#dse2.run_sets_question()
#dse2.demonstrateDicts()
#dse2.run_dict_question()

cse1 = ControlStructureEngine()
cse1.demonstrateIf()