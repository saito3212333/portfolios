import random

import numpy
import pandas as pd

class DataFrameEngine:
    def demonstrateDataFrames(self):
        # この場合、display.max_rowsオプションは、データフレームの最大表示行数を指定します。
        # Noneを指定することで、全ての行を表示するように設定されます。同様に、display.max_columnsオプションは、データフレームの最大表示列数を指定します。


        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

        city_names = ['Toronto', 'Sault Ste Marie', 'Windsor', 'Niagara', 'Oshawa', 'Hamilton']
        #　列名がcitynameの一列とインデックスのデータフレームになります。
        city_names_df = pd.DataFrame(city_names, columns=['city_names'])
        print(city_names_df)

        city_data = {
            'city_names' : ['Toronto', 'Sault Ste Marie', 'Windsor', 'Niagara', 'Oshawa', 'Hamilton'],
            'population_m' : [30, 0.7, 1.2, 2, 5, 4],
            'avg_annual_temp_c': [10.0, 4.0, 9.2, 8.4, 5.5, 9.8]
        }

        print()
        # 辞書型のデータを使用して、データフレームを作成し、表示します。
        city_df = pd.DataFrame(city_data)
        print(city_df)

        print()
        print("DATA EXTRACTION")
        print("city_names")
        #どっちでもいけるよという話。
        print(city_df.city_names)
        print()
        print("population_m")
        # どっちでもいけるよという話。
        print(city_df["population_m"])

        print()
        print("city_names, population_m")

        # 二つかっこで複数列を選べるよ。
        print(city_df[["city_names","population_m"]])

        print()
        print("population_m")
        # 行の選択ができるよ　ちなみにこれは　0,1,2

        print(city_df["population_m"][:3])

        print()
        print("city_names, population_m")
        # 複数列＋行の選択ができるよ　ちなみにこれは　0,1,2
        print(city_df[["city_names", "population_m"]][:3])

        print()
        # ilocを使用して、行や列の位置を指定してデータを抽出します。　数字のみ引数にする
        print(city_df.iloc[:3])
        print()
        print(city_df.iloc[2:3])
        print()
        # locを使用して、行や列のラベルを指定してデータを抽出します。左が行、右が列、列は名前でも可能
        print(city_df.loc[[0, 3, 5]])
        print()
        print(city_df.loc[[0, 3, 5]][["city_names", "population_m"]])

        print()

        # これは各行に適応されて、偽であれば表示させない。
        print(city_df[[True, True, False, False, True, False]])

        print()

        print(city_df[city_df.population_m > 3])

        print()
        print(city_df.head())
        print()
        print(city_df.tail())
        print()
        print(city_df.describe())
        print()
        # このINCLUDEは知らんかったなー
        print(city_df.describe(include='all'))

        print()
        print(city_df.index)

        # これはいいリスト内包ですね。そして、直でインデックスに入れれるんやー
        city_df.index = ['C'+str(i) for i in range(1,7)]
        print(city_df.index)
        print()
        print(city_df)

        # これでインデックスをリセット、いつ使うかな？
        city_df.reset_index(inplace=True)
        print()
        print(city_df)

        city_df.set_index('index',inplace=True)
        print()
        print(city_df)

        print()
        # iterrows()
        for a , b in city_df.iterrows():
            print(a, b)
            print()

        # itertuples()
        for t in city_df.itertuples():
            print(t)
            print()

    # iterrows():
    # iterrows()
    # は、データフレームの各行を反復処理するためのメソッドです。反復処理中に、
    # 各行のインデックスと行のデータをタプルとして返します。
    #
    # 戻り値は、反復ごとに次のようなタプルです:
    #
    # インデックス(行のラベル)
    # 行のデータを含むシリーズ
    # itertuples():
    # は、データフレームの各行を反復処理するためのメソッドです。反復処理中に、
    # 各行のデータを含む名前付きタプルを返します。
    #
    # 戻り値は、反復ごとに次のような名前付きタプルです:
    #
    # インデックス(行のラベル)
    # 各列の値を属性として持つ名前付きタ
    # プル

    # リスト内包表記のレンジは複数のデータを扱うためのもの。
    # ,これは便利！
    def demonstrateDFMethods(self):
        marks = pd.DataFrame({
            'name' : ['S'+str(i) for i in range(1,21)],
            'age' : [random.randint(18,40) for _ in range(20)],
            'marks1': [random.randint(20,50) for _ in range(20)],
            'marks2': [random.randint(20, 50) for _ in range(20)]
        })

        print(marks)

        # Add the total column / total = marks1+marks2
        # 多分、marks['marks1'] + marks['marks2']
        marks['total'] = marks.marks1 + marks.marks2
        print()
        print(marks)

        # 新しい列の追加、４列目にボーナスという列を追加、値はランダムで。
        marks.insert(4, 'bonus', [random.randint(1,5) for _ in range(20)])
        print()
        print(marks)

        # if total + bonus > 100 then total_with_bonus = 100, else total_with_bonus = total + bonus
        marks['total_with_bonus'] = numpy.where(marks['total'] + marks['bonus'] > 100, 100, marks['total'] + marks['bonus'])

        # numpy.where(condition, x, y)
        # condition: 条件式を指定します。この条件がTrueである要素が選択されます。
        # x: conditionがTrueの場合に返される値または配列です。
        # y: conditionがFalseの場合に返される値または配列です。


        # marks['total_with_bonus'] = marks.total + marks.bonus
        # marks['total_with_bonus'] = marks['total_with_bonus'].clip(upper=100)
        # .clip(upper=100)は、Pandasシリーズやデータフレームのメソッドの1つで、
        # 要素の値を上限値で切り捨てるために使用されます。
        #
        # 具体的には、upperパラメーターで指定された値を上限として、
        # 要素の値がそれを超える場合は上限値に設定され、超えない場合はそのままの値となります。



        print(marks)

        print()
        # No of unique 略してnunique() それぞれの列ごとのユニークなエンティティ数を返す。
        print(marks.nunique())
        print(marks.isna())

        # sort_values , sort_index で並び替え、これはデータフレームオブジェクトのメソッド。
        print(marks.sort_values(['total_with_bonus', 'name']))
        print(marks.sort_index())

        # 列名の変更方法、これもメソッド、辞書を使って複数変換も可能。インプレイスで調整
        marks.rename(columns={'name': 'student_name',
                      'age' : "student_age"}, inplace=True)
        print()
        print(marks)

        # ドロップメソッドで列を落とす。懐かしい。
        #marks.drop("name")
        print()

        # これでサンプルのデータを抽出できるやん。
        print(marks.sample(5))

        print()

        # メソッドです。タプルを返してくれる。（行、列）
        print(marks.shape)
        # 次元数を返す、今回であれば、２面
        print(marks.ndim)

        #dropna
        #marks.dropna()
        #fillna

        #　とりあえず複数列を指定するときは２重かっこ
        print(marks[['marks1' , 'marks2' , 'bonus' ,'total' , 'total_with_bonus']].mean())
        #marks.fillna(marks.mean())

        # これは、marksデータフレーム内のNaN値を各列の平均値で置き換えます。
        # ただし、この操作は元のデータフレームを変更しません。
        # 元のデータフレームを変更するには、inplace = Trueを追加する必要があります。

        marks['total_with_bonus'].where(marks.total_with_bonus >= 60, 60, inplace=True)
        # print(marks)

        marks['total_with_bonus'] = marks['total_with_bonus'].where(marks.total_with_bonus >= 60, 60)
        print(marks)

        print(marks.duplicated())
        print(marks.drop_duplicates())






dfe1 = DataFrameEngine()
#dfe1.demonstrateDataFrames()
dfe1.demonstrateDFMethods()