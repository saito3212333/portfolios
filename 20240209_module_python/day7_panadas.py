import random
import random as rd
import statistics as st
import string

import numpy as np
import pandas as pd

import tkinter as tk
from tkinter import filedialog

import sqlalchemy
from sqlalchemy import text


class PandasEngine:
    def demonstrateStats(self):
        age = [rd.randint(18, 60) for _ in range(20)]
        salary = [int(3000 + rd.uniform(0, 1) * 50 * a - 18) for a in age]

        print('AGE:', age)
        print('SALARY:', salary)

        # mean: Arithmetic mean (average) of data.
        print()
        print("MEAN")
        print('MEAN AGE:', st.mean(age))
        print('MEAN SALARY:', st.mean(salary))

        # median: Median (middle value) of data.
        print()
        print("MEDIAN")
        print('MEDIAN AGE:', st.median(age))
        print('MEDIAN SALARY:', st.median(salary))

        # mode: Mode (most common value) of data.
        print()
        print("MODE")
        print('MODE AGE:', st.mode(age))
        print('MODE SALARY:', st.mode(salary))

        # multimode: List of modes (most common values of data).
        print()
        print("MULTIMODE")
        print('MULTIMODE AGE:', st.multimode(age))
        print('MULTIMODE SALARY:', st.multimode(salary))

        # quantiles: Divide data into intervals with equal probability.
        print()
        print("QUANTILES")
        print('4 QUARTILES AGE:', st.quantiles(age, n=4))
        print('4 QUARTILES SALARY:', st.quantiles(salary, n=4))

        # stdev : Sample standard deviation of data.
        print()
        print("STDEV")
        print('STDEV AGE:', st.stdev(age))
        print('STDEV SALARY:', st.stdev(salary))

        # covariance: Sample covariance for two variables.
        print()
        print("COVARIANCE")
        print('COVARIANCE AGE vs. SALARY:', st.covariance(age, salary))

        # correlation: Pearson's correlation coefficient for two variables.
        print()
        print("CORRELATION")
        print('CORRELATION AGE vs. SALARY:', st.correlation(age, salary))

        # correlation: Spearman's Ranked correlation coefficient for two variables.
        print()
        print("CORRELATION")
        print('CORRELATION AGE vs. SALARY:', st.correlation(age, salary, method = 'ranked'))

        # sum:
        print()
        print("SUM")
        print('SUM AGE:', sum(age))
        print('SUM SALARY:', sum(salary))

        # max:
        print()
        print("MAX")
        print('MAX AGE:', max(age))
        print('MAX SALARY:', max(salary))

        # min:
        print()
        print("MIN")
        print('MIN AGE:', min(age))
        print('MIN SALARY:', min(salary))

        # numpy:
        print()
        print("Log")
        print('LOG of AGE:', np.log(age))
        print('LOG of  SALARY:', np.log(salary))



    def demonstrateSeries(self):
        #filepath = filedialog.askopenfilename()
        mall_df = pd.read_csv("D:\\Tsom\\PData\\Mall_Customers.csv")
        print(mall_df)

        marks_l = [random.randint(40, 100) for _ in range(10)]
        marks_sr = pd.Series(marks_l)
        print()
        print(marks_l)
        print()
        print(marks_sr)

        prod_ids_sr = pd.Series(['001111', 123221, '0092122', 132134, 3554322])
        print()
        print(prod_ids_sr)

        print()
        print("Series Subsetting")
        print(marks_sr[7]) #8th Observation --> Single Data Point, INT
        print(marks_sr[:5])  # from the first to the 5th Observation --> Output is a series
        print(marks_sr[5:])  # from the 5th Observation to the last --> Output is a series

        print(marks_sr.index)

        # ['P1',  P2',P3',P4',P5']
        prod_ids_sr = pd.Series(['001111', 123221, '0092122', 132134, 3554322],
                                index = [ 'P' + str(i+1) for i in range(5)])
        print()
        print(prod_ids_sr)
        print()
        print(prod_ids_sr['P2'])

        print(prod_ids_sr[['P2','P4']])

        print()
        marks2 = {"S1":56,"S2":56,"S3":87, "S4":76, "S5":99}
        marks2Series2 = pd.Series(marks2)
        print(marks2Series2)

        marks2Series3 = pd.Series(marks2, index=["S1","S2"])
        print(marks2Series3)


    def demonstrate_series_operations(self):
        # Marks of 15 students, randomly generated. Use A1, B2, C3 ... as Studnet names. Generate this random Series.
        sr_marks1 = pd.Series({ string.ascii_uppercase[i]+str(i): rd.randint(40, 100)   for i in range(1,16)})
        sr_marks2 = pd.Series({string.ascii_uppercase[i] + str(i): rd.randint(40, 100) for i in range(1, 16)})


        print(" STUDENT MARKS")
        print(" MARKS 1")
        print(sr_marks1)
        print()
        print(" MARKS 2")
        print(sr_marks2)

        print()
        print(sr_marks1 + sr_marks2)
        print()
        print(sr_marks1 * 1.1)

        print()
        list1 = [rd.randint(20, 50) for _ in range(10)]
        list2 = [rd.randint(20, 50) for _ in range(10)]
        print(list1)
        print(list2)
        print(list1+list2)

        print()
        print("Total Marks:", sr_marks1.add(sr_marks2))
        print("Marks1:", sr_marks1)

        sr_total = sr_marks1.add(sr_marks2)
        print("Total Marks:", sr_total)

        mean_total = sr_total.mean()
        total_total = sr_total.sum()

        print()
        print("Class Total:", total_total, " | Class Avg:", mean_total)

        print("Count:" , sr_total.count())
        print("Count:", sr_total.size)

        print()
        print("First Few Obs.: \n", sr_total.head(3))
        print()
        print("Last Few Obs.: \n", sr_total.tail(3))

        print()
        print(sr_total.sort_values())
        print(sr_total.sort_index())

        print(sr_total.is_unique)

        print()
        print(sr_marks1.ge(sr_marks2)) # The output is a Series of bool values
        print()
        print(sr_marks1 >= sr_marks2)  # The output is a Series of bool values

        print()
        print(sr_total)
        print(sr_total.clip(150))

        print()
        print(sr_total.unique())

        print(sr_total.between(100, 150))

        sr_avg_marks = (sr_marks1 + sr_marks2 ) / 2

        def grade_the_marks(num1):
            if(num1 >= 80): return 'A'
            elif (num1 >= 70): return 'B'
            elif (num1 >= 60): return 'C'
            else: return 'F'

        print(sr_avg_marks)
        print(sr_avg_marks.apply(grade_the_marks))













    def demonstrateMySQLDataAccess(self):
        # sqlalchemy
        # pymysql
        # cryptography
        # mysql+pymysql://<username>:<password>@<server>/<database>

        password = input("Enter your password")
        db_engine = sqlalchemy.create_engine("mysql+pymysql://root:",password,"@localhost/test1")
        conn = db_engine.connect()
        print(conn)

        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

        df = pd.read_sql(text('SELECT * FROM test1.buyers'), conn)
        print(df)
        conn.close()




pe1 = PandasEngine()
#pe1.demonstrateStats()
#pe1.demonstrateSeries()
#pe1.demonstrateMySQLDataAccess()
pe1.demonstrate_series_operations()