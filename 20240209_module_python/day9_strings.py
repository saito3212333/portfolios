import string
from collections import Counter

import numpy
import pandas as pd


class ExEngine:
    def do_df_ex(self):
        """Using mallC, answer the following questions:"""
        mallC = pd.read_csv(".\\Data\\Mall_Customers.csv")
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print(mallC)

        """Add a column call annual_income_usd by multiplying the existing Annual Income column by 1000. """
        mallC.columns = ['CustomerID', 'Gender', 'Age', 'Annual_Income_k_USD', 'Spending_Score']
        print("####Q1####")
        mallC["annual_income_usd"] = mallC.Annual_Income_k_USD * 1000
        print(mallC.head())

        print()
        """What is the average age and income of the population?"""
        print("Average Age:" + str(mallC.Age.mean()) +
              " | Average Income:" + str(mallC.Annual_Income_k_USD.mean()))

        print()
        """List the top 20 observations after sorting them by Annual Income (Ascending – lowest income first)."""
        print(mallC.sort_values("Annual_Income_k_USD").head(20))

        print()
        """Generate and print another dataframe listing all the female customers who's age is greater than or equal to 40."""
        mallC_f_gt_40 = mallC[list(mallC.Age >= 40) and list(mallC.Gender == 'Female')]
        mallC_f_gt_40 = mallC[(mallC.Age >= 40) & (mallC.Gender == 'Female')]
        print(mallC_f_gt_40)

        print()
        """Add another variable called 'spend_index' whereas spend_index = spending score / annual income. """
        mallC.insert(loc=6, column="spend_index", value=mallC.Spending_Score / mallC.Annual_Income_k_USD)
        print(mallC.head())

        print()
        """Generate and print another dataframe listing all the male customers who's age is greater than or equal to 40 and annual income is '
                                                                                'above the 75th percentile of the range.)"""
        income75 = numpy.percentile(mallC.Annual_Income_k_USD, 0.75)
        mallCm_gt_40 = mallC[(mallC.Age >= 40) & (mallC.Gender == 'Male') &
                             (mallC.Annual_Income_k_USD > income75)]
        print(mallCm_gt_40)

        print()
        """Add another variable called 'income_outlier' which is a flag (True/ False) to indicate if the income value is an outlier in the range. 
        Use the standard IQR based calculation to determine the outliers and populate the income_outlier column. """
        incomeQ3 = numpy.percentile(mallC.Annual_Income_k_USD, 0.75)
        incomeQ1 = numpy.percentile(mallC.Annual_Income_k_USD, 0.25)
        incomeIQR = incomeQ3 - incomeQ1
        mallC["income_outlier"] = ((mallC.Annual_Income_k_USD < incomeQ1 - 1.5 * incomeIQR)
                                   | (mallC.Annual_Income_k_USD > incomeQ3 + 1.5 * incomeIQR))
        print(mallC.head())
        print(mallC[mallC.income_outlier == True])

        print()
        """For each observation, print the following if the customer is female, under 25 of age, and spend index is greater than or equal to 1.00.
        Customer <ID> is a Potential Female Candidate with a spend index <spend_index>"""
        print()

        for i, j in mallC.iterrows():
            if (j["spend_index"] >= 1 and j["Gender"] == 'Female' and j["Age"] < 25):
                print("Customer", j["CustomerID"], " is a Potential Female Candidate with a spend index ",
                      round(j["spend_index"], 2))


class StringEngine:
    def recapStringBasics(self):
        text1 = """It urged that the next Legislature "provide enabling funds
        and re-set the effective date so that an orderly implementation of the law may be effected"."""

        print(text1)
        sbstr1 = text1[:8]
        print(sbstr1)

        int1 = 45
        bool1 = True
        print(sbstr1, int1, bool1)
        sbstr2 = sbstr1 + ' ' + str(int1) + ' ' + str(bool1)
        print(sbstr2)

        # start:stop:step
        print(sbstr2[::-1])
        print(''.join(list(reversed(sbstr2))))
        print(sbstr2[::2])
        print()
        print()

        # STRING FORMATTING
        name = 'Emmanuel'
        age = 43
        nationalty = 'Canadian'

        # greeting = 'Hello, '+ name + '. It is good to know that you are ' + age + ' and ' + nationalty + '.'
        greeting = 'Hello, {}. It is good to know that you are {} and {}.'
        print(greeting.format(name, age, nationalty))

        greeting2 = 'Hello, {2}. It is good to know that you are {0} and {1}.'
        print(greeting2.format(age, nationalty, name))

        greeting3 = 'Hello, {a}. It is good to know that you are {b} and {c}.'
        print(greeting3.format(b = age, c = nationalty, a = name))

        print('\n\n')
        car = 'Honda'
        model = 'CRV 2024'
        price = 42000
        discount = -2000

        car_str = 'We can offer you a {0} {1} for ${2:,.2f}  with a discount of {3:,.2f}.'
        print(car_str.format(car, model,price, discount ))
        print('binary format: {:b}'.format(discount))
        print('decimal format: {:d}'.format(discount))
        print('octal format: {:o}'.format(discount))
        print('hex format: {:x}'.format(discount))

        print()
        print(f'We can offer you a {car} {model} for ${price:,.2f}  with a discount of {discount:,.2f}.')
        print(f'''We can offer you a {car} {model} for ${price:,.2f}  with a discount of {discount:,.2f}.
                After discount, the price would be ${price+discount:,.2f}.''')
        print()
        print(f'The sqr. root of 2 is {round(numpy.sqrt(2), 3)},')

        print()
        print("I have \"two\" dogs.")
        print("folder1\\filename")

        print()
        str1 = f'The sqr. root of 2 is {round(numpy.sqrt(2), 3)}.'
        print(str1)
        print(str1.upper()) # ALl CAPS
        print(str1.lower()) # all simple
        print(str1.swapcase()) # Case switched
        print(str1.capitalize()) # First letter capitalized
        print(str1.title()) # The first letter of each word capitalized

        print()
        str2 = f'    The sqr. root of 2 is {round(numpy.sqrt(2), 3)}.    '
        print(str1)
        print(str2)
        print(str2.strip())
        print(str2.lstrip())
        print(str2.rstrip())

        print()
        str2 = 'I like apples. Sometimes apples are red, and sometimes apples are green.'
        print(str2.find('apples'))
        print(str2.index('apples', 0, 15))

        print(str2.rfind('apples'))

        print()
        print(str2.isalpha())

        str3 = '76.4'
        str4 = '9'
        str5 = 'bread'
        print()
        print(str3.isalpha())
        print(str4.isalpha())
        print(str5.isalpha())

        print()
        print(str3.isdigit())
        print(str4.isdigit())
        print(str5.isdigit())

        print()
        print(str3.isalnum())
        print(str4.isalnum())
        print(str5.isalnum())

        print()
        print(str3.isdecimal())
        print(str4.isdecimal())
        print(str5.isdecimal())

        print()
        print(str3.isascii())
        print(str4.isascii())
        print(str5.isascii())

        print()
        str6 = '''We cordially invite our current and former students, 
         well as members of the wider TSoM community, to participate in 
         our upcoming events and take advantage of these exceptional opportunities.'''
        print(str6)
        print(str6.lower().count('the'))
        print(str6.replace('TSoM', 'NCT'))
        print()

        # EXTRACT THE WORDS/TOKENS
        print(str6.split())

        # EXTRACT THE UNIQUE WORDS/TOKENS
        lst_words = set(str6.split())
        print(lst_words)

        print()
        str7 = '''Students will be offered paid or unpaid entry-level positions 
        related to their field of studies. The Career Services Department will 
        provide full support to students on booking and preparing for interviews. 
        It is the student’s responsibility to perform well during all interviews as 
        well as during the full length of the co-op term. Placements are subject 
        to availability and will vary based on the program, season and job market 
        changes as well as the student’s English level and previous professional 
        and academic experience. Should the co-op placement not be available the 
        student will be required to complete a Capstone Project as an alternative 
        to graduate from the program.'''

        # EXTRACT THE COUNT/FREQUENCY OF UNIQUE WORDS/TOKENS
        print()
        bow_str7 = str7.lower().split()
        word_count = Counter(bow_str7)
        print(word_count)
        print()
        word_count_dict = dict(word_count)
        print()

        word_count_dict_sorted = dict(sorted(word_count_dict.items(), reverse= True,
                                        key = lambda item : item[1]))

        print(word_count_dict_sorted)

        print()
        lst_str8 = 'It is a beautiful day.'.split()
        print(lst_str8)
        print('Kazuki'.join(lst_str8))
        print(' '.join(lst_str8))

        print()
        lst1 = ['a', 'b', 'c']
        lst2 = [5,6,10]

        z_list = zip(lst1, lst2)
        print(z_list)
        print(list(z_list))
        z_list = zip(lst1, lst2)
        print(dict(z_list))

        print()
        # CONSTANTS

        print('ascii_uppercase: ', string.ascii_uppercase)
        print('ascii_lowercase: ', string.ascii_lowercase)
        print('ascii_letters: ', string.ascii_letters)
        print('punctuation: ', string.punctuation)
        print('digits: ', string.digits)

    def doTokenTask(self):
        text1 = '''Before we get into more details about the different types of paragraph, let’s explain what a paragraph really is. No, five consecutive sentences don’t make up a paragraph. And no, a paragraph doesn’t have to be half a page long. So, what is a paragraph? Regardless of all the paragraph organization types, the definition of a paragraph is pretty simple. A paragraph is a “group of sentences or a single sentence that forms a unit” (Lunsford and Connors, 1995, p.116).'''
        # Split the text into a list of words and call it xWords.
        # Remove extra white spaces in all the words in xWords.
        # Remove any special character in all the words in xWords by replacing it with
        # a space character. For instance, if a word is 'person"'
        # the result should replace it with person.
        xWords = text1.lower().split()
        xWords = [i.strip() for i in xWords]

        text2 = ' '.join(xWords)
        text2_lst = list(text2)

        counter = 0
        for c in text2_lst:
            if not(c.isalnum()):
                print(counter)
                text2_lst[counter] = ' '

            counter += 1

        text3 = ''.join(text2_lst)
        print(text3)

        xWords = text1.lower().split()







ee2 = ExEngine()
#ee2.do_df_ex()
se1 = StringEngine()
#se1.recapStringBasics()
se1.doTokenTask()