import string
from collections import Counter

import numpy
import pandas as pd


class ExEngine:
    def do_df_ex(self):
        """Using mallC, answer the following questions:"""
        # windows .\\___\\
        mallC = pd.read_csv("./data/Mall_Customers.csv")
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print(mallC.head())
        print(mallC.shape)

        """Add a column call annual_income_usd by multiplying the existing Annual Income column by 1000. """
        # 直接５個列の名前を指定してあげて名前の変更、
        mallC.columns = ['CustomerID', 'Gender', 'Age', 'Annual_Income_k_USD', 'Spending_Score']
        print("####Q1####")

        # 新しい列を追加していますね。
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
        print("####Q1-1####")
        """Generate and print another dataframe listing all the female customers who's age is greater than or equal to 40."""
        mallC_f_gt_40 = mallC[list(mallC.Age >= 40) and list(mallC.Gender == 'Female')]

        # 条件式ですね。
        mallC_f_gt_40 = mallC[(mallC.Age >= 40) & (mallC.Gender == 'Female')]
        print(mallC_f_gt_40.head())

        print()

        # インサートと直接入れるやつの違いは、何列目に入れるか指定できる、明示的にわかりやすい、
        """Add another variable called 'spend_index' whereas spend_index = spending score / annual income. """
        mallC.insert(loc=6, column="spend_index", value=mallC.Spending_Score / mallC.Annual_Income_k_USD)
        print(mallC.head())


        """Generate and print another dataframe listing all the male customers who's age is greater than or equal to 40 and annual income is '
                                                                                'above the 75th percentile of the range.)"""
        # パーセンタイルを０.７５を算出
        income75 = numpy.percentile(mallC.Annual_Income_k_USD, 0.75)
        print(income75)

        # ３つの条件式の条件式ですね。
        mallCm_gt_40 = mallC[(mallC.Age >= 40) & (mallC.Gender == 'Male') &
                             (mallC.Annual_Income_k_USD > income75)]
        print(mallCm_gt_40.head())

        print()
        """Add another variable called 'income_outlier' which is a flag (True/ False) to indicate if the income value is an outlier in the range. 
        Use the standard IQR based calculation to determine the outliers and populate the income_outlier column. """
        incomeQ3 = numpy.percentile(mallC.Annual_Income_k_USD, 0.75)
        incomeQ1 = numpy.percentile(mallC.Annual_Income_k_USD, 0.25)
        # 出た、IQR　と外れ値
        incomeIQR = incomeQ3 - incomeQ1
        mallC["income_outlier"] = ((mallC.Annual_Income_k_USD < incomeQ1 - 1.5 * incomeIQR)
                                   | (mallC.Annual_Income_k_USD > incomeQ3 + 1.5 * incomeIQR))
        print(mallC.head())
        print(mallC[mallC.income_outlier == True].head())

        print()
        """For each observation, print the following if the customer is female, under 25 of age, and spend index is greater than or equal to 1.00.
        Customer <ID> is a Potential Female Candidate with a spend index <spend_index>"""
        print()
        # i がインデックス　jがオブザベーションが縦になって返ってくる
        for i, j in mallC.iterrows():
            if (j["spend_index"] >= 1 and j["Gender"] == 'Female' and j["Age"] < 25):
                print("Customer", j["CustomerID"], " is a Potential Female Candidate with a spend index ",
                      round(j["spend_index"], 2))

class StringEngine:
    def recapStringBasics(self):
        text1 = """It urged that the next Legislature "provide enabling funds
        and re-set the effective date so that an orderly implementation of the law may be effected"."""

        print(text1)
        # 0--7 の８個を抽出
        sbstr1 = text1[:8]
        print(sbstr1)

        int1 = 45
        bool1 = True
        print(sbstr1, int1, bool1)
        sbstr2 = sbstr1 + ' ' + str(int1) + ' ' + str(bool1)
        print(sbstr2)

        # start:stop:step
        print(sbstr2[::-1])
        # リバースで逆むけて、リストでリストに、最後にジョイン
        print(list(reversed(sbstr2)))
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

        # ${2:,.2f}: price変数の値が挿入されます。この値は、3桁ごとにカンマが挿入され、小数点以下2桁まで表示されます。
        # {3:,.2f}: discount変数の値が挿入されます。同様に、3桁ごとにカンマが挿入され、小数点以下2桁まで表示されます。
        car_str = 'We can offer you a {0} {1} for ${2:,.2f}  with a discount of {3:,.2f}.'
        print(car_str.format(car, model,price, discount ))
        print('binary format: {:b}'.format(discount))
        print('decimal format: {:d}'.format(discount))
        print('octal format: {:o}'.format(discount))
        print('hex format: {:x}'.format(discount))
        # それぞれ、データをバイナリ、10進、8進、16進形式に変換して表示します。
        # {: b}はバイナリ、{: d}は10進、{: o}は8進、{: x}は16進形式を表します。
        #

        print()
        print(f'We can offer you a {car} {model} for ${price:,.2f}  with a discount of {discount:,.2f}.')
        print(f'''We can offer you a {car} {model} for ${price:,.2f}  with a discount of {discount:,.2f}.
                After discount, the price would be ${price+discount:,.2f}.''')
        print()
        print(f'The sqr. root of 2 is {round(numpy.sqrt(2), 3)},')

        # \をつければ、特殊文字を表示できますねー
        print()
        print("I have \"two\" dogs.")
        print("folder1\\filename")

        print()
        str1 = f'The sqr. root of 2 is {round(numpy.sqrt(2), 3)}.'
        print(str1)
        print(str1.upper()) # ALl CAPS
        print(str1.lower()) # all simple
        print(str1.swapcase()) # Case switched　大文字を小文字に小文字を大文字に。
        print(str1.capitalize()) # First letter capitalized
        print(str1.title()) # The first letter of each word capitalized　文字それぞれの先頭を大文字に

        print()
        str2 = f'    The sqr. root of 2 is {round(numpy.sqrt(2), 3)}.    '
        print(str1)
        print(str2)
        print(str2.strip())#str2の前後の空白を削除して表示します。
        print(str2.lstrip())#str2の左側の空白を削除して表示します。
        print(str2.rstrip())#str2の右側の空白を削除して表示します。

        print()
        str2 = 'I like apples. Sometimes apples are red, and sometimes apples are green.'

        # find()メソッドは、指定された部分文字列（この場合は'apples'）が
        # 最初に見つかったインデックスを返します。もし見つからない場合は、-1を返します。
        # この行では、最初に'apples'が見つかったインデックスを表示します。
        print(str2.find('apples'))

        # index()メソッドは、指定された部分文字列が最初に見つかったインデックスを返しますが、
        # 見つからない場合はValueErrorを発生させます。第二引数と第三引数は探索範囲を指定します。
        # この行では、最初の15文字内で'apples'が見つかったインデックスを表示します。
        print(str2.index('apples', 0, 15))

        # rfind()メソッドは、指定された部分文字列が最後に見つかったインデックスを返します。
        # この行では、最後に'apples'が見つかったインデックスを表示します。
        print(str2.rfind('apples'))

        print()

        # アルファベットだけで構成されていますか？
        print(str2.isalpha())
        print('abc'.isalpha())

        str3 = '76.4'
        str4 = '9'
        str5 = 'bread'
        print()
        print(str3.isalpha())
        print(str4.isalpha())
        print(str5.isalpha())

        # これは数字のみ.もだめです。
        print()
        print(str3.isdigit())
        print(str4.isdigit())
        print(str5.isdigit())
        # アルファベットもしくは数字
        print()
        print(str3.isalnum())
        print(str4.isalnum())
        print(str5.isalnum())

        # １０進数のみです。
        print()
        print(str3.isdecimal())
        print(str4.isdecimal())
        print(str5.isdecimal())
        #isascii()メソッドは、文字列がASCII文字のみで構成されているかどうかを示すブール値を返します。
        # str3、str4、str5のすべての文字はASCII文字であるため、すべての場合にTrueが返されます。
        print()
        # print(str3.isascii())
        # print(str4.isascii())
        # print(str5.isascii())

        print()
        str6 = '''We cordially invite our current and former students, 
         well as members of the wider TSoM community, to participate in 
         our upcoming events and take advantage of these exceptional opportunities.'''
        print(str6)
        print(str6.lower().count('the'))
        print(str6.replace('TSoM', 'NCT'))
        print()

        # EXTRACT THE WORDS/TOKENS
        # split()メソッドを使用して、文字列を空白文字で分割します。
        # 結果はリストとして返されます。
        print(str6.split())

        # EXTRACT THE UNIQUE WORDS/TOKENS
        # split()メソッドで文字列を空白文字で分割し、
        # その後重複を除去するためにset()関数を使用します。
        # セットで重複削除できるんですね。知らんかった。

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
        # 肝はcounter関数
        word_count = Counter(bow_str7)

        print('_______________________')
        # <class 'collections.Counter'>　これがデータタイプです。
        print(type(word_count))
        print(word_count)
        print()
        # 　辞書にしてあげるといい感じになります。
        word_count_dict = dict(word_count)
        print()
        # sorted()関数は、指定されたイテラブル
        # （ここではword_count_dict.items()で
        # 辞書のキーと値のペアがイテレートされます）をソートします。
        # reverse=True引数により、降順（大きい値から小さい値へ）でソートされます。
        # key引数は、ソートの際に使用される関数またはキー関数を指定します。
        # ここでは、lambda関数を使用して各アイテムの値（item[1]）をキーとして指定しています。
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
        print('this is ',z_list)
        print(list(z_list))
        z_list = zip(lst1, lst2)
        print(dict(z_list))
        # イテレーター（iterator）は、要素を1つずつ順番に提供するオブジェクトです。
        # イテレーターは主にループや反復処理に使用されます。
        # Pythonでは、多くの場面でイテレーターが使用されますが、特にforループやzip()、
        # enumerate()、map()、filter()などの組み込み関数でよく見られます。
        #
        # イテレーターは、iter()関数で生成されるオブジェクトで、
        # next()関数を使用して次の要素に進むことができます。
        # また、forループを使うことで、イテレーターから要素を順番に取り出すこともできます。
        print()
        # CONSTANTS
        # 特殊文字の扱い方。
        print('ascii_uppercase: ', string.ascii_uppercase)
        print('ascii_lowercase: ', string.ascii_lowercase)
        print('ascii_letters: ', string.ascii_letters)
        print('punctuation: ', string.punctuation)
        print('digits: ', string.digits)

        # ascii_uppercase:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
        # ascii_lowercase:  abcdefghijklmnopqrstuvwxyz
        # ascii_letters:  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        # punctuation:  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        # digits:  0123456789
    def doTokenTask(self):
        text1 = '''Before we get into more details about the different types of paragraph, let’s explain what a paragraph really is. No, five consecutive sentences don’t make up a paragraph. And no, a paragraph doesn’t have to be half a page long. So, what is a paragraph? Regardless of all the paragraph organization types, the definition of a paragraph is pretty simple. A paragraph is a “group of sentences or a single sentence that forms a unit” (Lunsford and Connors, 1995, p.116).'''
        # Split the text into a list of words and call it xWords.
        # Remove extra white spaces in all the words in xWords.
        # Remove any special character in all the words in xWords by replacing it with
        # a space character. For instance, if a word is 'person"'
        # the result should replace it with person.
        print(text1)
        xWords = text1.lower().split()# 全部小文字にしてスプリット
        xWords = [i.strip() for i in xWords] # 空白を削除　スプリットされた一文字ずつ
        print(xWords)
        text2 = ' '.join(xWords)#また結合
        text2_lst = list(text2)#リスト化したら１文字ずつ格納
        print(text2_lst)
        counter = 0
        for c in text2_lst:
            # のっと　＋　（）が必要です。
            if not(c.isalnum()):
                #print(counter)
                text2_lst[counter] = ' '
                # c = ' '
            counter += 1

        text3 = ''.join(text2_lst)
        print(text3)

        xWords = text1.lower().split()







#ee2 = ExEngine()
#ee2.do_df_ex()
se1 = StringEngine()
#se1.recapStringBasics()
se1.doTokenTask()