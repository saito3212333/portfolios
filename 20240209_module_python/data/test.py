# import pandas as pd
#
# data = dict(name = ['Kevin', 'Danny', 'Henry', 'Kis', 'Polar',  'Vik', 'Rog'],
#             marks = [50, 40, 45,35,24,43, 26], age = [24, 25, 21,26,27,29, 23])
# df = pd.DataFrame(data, index = ["S1","S2","S3","S4","S5","S6","S7"])
#
# print(df[1])
#
# #print(df.iloc(1))
#
# #print(df.name)
#
# #print(df.name[1])
#
# #print(df.iloc[1:9])
#
# #print(df.iloc[1])
#
# import pandas as pd
# import statistics as st
#
# data = dict(name = ['Kevin', 'Danny', 'Henry', 'Kis', 'Polar',  'Vik', 'Rog'],
#             marks = [50, 40, 45,35,24,43, 26],
#             age = [24, 25, 21,26,27,29, 23])
# df = pd.DataFrame(data, index = ["S1","S2","S3","S4","S5","S6","S7"])
# print(df)
# dic = dict()
# def getMarksOfPeople(marksData, minAge):
#     mean_age = st.mean(marksData['age'])
#     for age in marksData['age']:
#         if age >= minAge:
#             dic.update({index : age})

#Accept one dataframe object (marksData) and one integer (minAge) as input parameters.
#Return a dictionary, keys of which are the index labels and values are the marks of the observation of marksData where age >= minAge.
#print(getMarksOfPeople(df,27))
# {'S5': 24, 'S6': 43}


# import pandas as pd
#
#
# data = dict(name=['Kevin', 'Danny', 'Henry', 'Kis', 'Polar', 'Vik', 'Rog'],
#             marks=[50, 40, 45, 35, 24, 43, 26],
#             age=[24, 25, 21, 26, 27, 29, 23])
# df = pd.DataFrame(data, index=["S1", "S2", "S3", "S4", "S5", "S6", "S7"])
# #print(df)
#
# def getMarksOfPeople(marksData, minAge):
#     new_dec = {}
#     for index, age in zip(marksData.index, marksData['age']):
#         if age >= minAge:
#             new_dec[index] = marksData.loc[index, 'marks']
#     return new_dec
#
# result = getMarksOfPeople(df, 25)
# print(result)

# import pandas as pd
#
# data = dict(name=['Kevin', 'Danny', 'Henry', 'Kis', 'Polar', 'Vik', 'Rog'],
#             marks=[50, 40, 45, 35, 24, 43, 26],
#             age=[24, 25, 21, 26, 27, 29, 23])
# df = pd.DataFrame(data, index=["S1", "S2", "S3", "S4", "S5", "S6", "S7"])
#
#
# def transformData(marksData):
#     # add new column
#     marksData['marks100'] = marksData['marks'] * 2
#     # add new column with list comprehension.
#     marksData['result'] = ['Pass' if marks >= 60 else 'Fail' for marks in marksData['marks100']]
#     return marksData
#
#
# print(transformData(df))

# complete the trasformData function to do the following:
#

# Add a new column to marksData called marks100 to indicate the marks out of 100.
# Add a new column to  marksData to set the standing of each student: 'Pass' if marks100 >= 60, and 'Fail' if not.
# Print marksData.

import pandas as pd
import statistics as st

data = dict(name=['Kevin', 'Danny', 'Henry', 'Kis', 'Polar', 'Vik', 'Rog'],
            marks=[50, 40, 45, 35, 24, 43, 26],
            age=[24, 25, 21, 26, 27, 29, 23])
df = pd.DataFrame(data, index=["S1", "S2", "S3", "S4", "S5", "S6", "S7"])


def printStudentsWithAboveAVGMarks(marksData):
    average_marks = st.mean(marksData['marks'])
    # iterrows will return the tuple including index and data of the observation.
    for index, row in marksData.iterrows():
        if row['marks'] > average_marks:
            print('Student with the ID (Index) ', index, ' scored ', row['marks'], ' marks')


printStudentsWithAboveAVGMarks(df)

# Complete the printStudentsWithAboveAVGMarks function to do the following:
#
# Run a DataFrame iteration to print the following for each observation  if the student's mark is greater than or equal to the average of the marks variable of the DataFrame:
# Student with the ID (Index) <Row Index> scored <Marks> marks