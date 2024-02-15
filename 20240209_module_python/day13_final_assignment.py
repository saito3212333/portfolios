import collections
import re
import string
import random as rd
import nltk
from nltk import stem
from nltk.corpus import stopwords
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from wordcloud import wordcloud

class ClothingReviewProject:

    reviews_all = pd.DataFrame()
    def run_project_wrok(self):
        self.loadData()
        self.reviews_all = self.cleanData(self.reviews_all)
    def loadData(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.reviews_all = pd.read_csv("./data/clothingReviews.csv")
        print(self.reviews_all.head())
        print(self.reviews_all.describe(include='all'))
    def cleanData(self, reviews_df):
            reviews_df.columns = ['idx', 'ClothingID', 'Age', 'Title', 'ReviewText',
                                'Rating', 'RecIND', 'PosFeedbackCount', 'DivisionName', 'DepartmentName',
                                'ClassName']
        print(reviews_df.describe(include='all'))
        print("***Number of Rows:", len(reviews_df))
        print()

        reviews_df.dropna(subset=['Rating', 'ReviewText'], inplace=True)
        print("***Number of Rows:", len(reviews_df))
        print()
        reviews_df = reviews_df[['Title', 'ReviewText', 'Rating', 'DivisionName', 'DepartmentName', 'ClassName']]
        print(reviews_df)
        print()
        return reviews_df

crp1 = ClothingReviewProject()
crp1.run_project_wrok()