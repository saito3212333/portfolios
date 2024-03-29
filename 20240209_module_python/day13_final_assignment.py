# import collections
# import re
# import string
# import random as rd
# import nltk
# from nltk import stem
# from nltk.corpus import stopwords
# import pandas as pd
# import plotly.express as px
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# from wordcloud import wordcloud
#
# class ClothingReviewProject:
#
#     reviews_all = pd.DataFrame()
#     def run_project_wrok(self):
#         self.loadData()
#         self.reviews_all = self.cleanData(self.reviews_all)
#     def loadData(self):
#         pd.set_option('display.max_columns', None)
#         pd.set_option('display.max_rows', None)
#         self.reviews_all = pd.read_csv("./data/clothingReviews.csv")
#         print(self.reviews_all.head())
#         print(self.reviews_all.describe(include='all'))
#     def cleanData(self, reviews_df):
#             reviews_df.columns = ['idx', 'ClothingID', 'Age', 'Title', 'ReviewText',
#                                 'Rating', 'RecIND', 'PosFeedbackCount', 'DivisionName', 'DepartmentName',
#                                 'ClassName']
#         print(reviews_df.describe(include='all'))
#         print("***Number of Rows:", len(reviews_df))
#         print()
#
#         reviews_df.dropna(subset=['Rating', 'ReviewText'], inplace=True)
#         print("***Number of Rows:", len(reviews_df))
#         print()
#         reviews_df = reviews_df[['Title', 'ReviewText', 'Rating', 'DivisionName', 'DepartmentName', 'ClassName']]
#         print(reviews_df)
#         print()
#         return reviews_df
#
# crp1 = ClothingReviewProject()
# crp1.run_project_wrok()


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
    stopWords = []

    def run_project_wrok(self):
        self.loadData()
        self.reviews_all = self.cleanData(self.reviews_all)
        self.analyseRating()
        self.stopWords = self.getStopWords()
        self.analyzeSentiments()

    def loadData(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        """ Load data into reviews_all. """
        self.reviews_all = pd.read_csv("./data/clothingReviews.csv")

        """ To understand the structure print the head of the DataFrame. """
        print(self.reviews_all.head())
        print(self.reviews_all.describe(include='all'))

    def cleanData(self, reviews_df):
        """ Transform column names and run summary stats to understand the variables more.
                Ensure to print the number of rows separately. """

        reviews_df.columns = ['idx', 'ClothingID', 'Age', 'Title', 'ReviewText',
                              'Rating', 'RecIND', 'PosFeedbackCount', 'DivisionName', 'DepartmentName',
                              'ClassName']

        print(reviews_df.describe(include='all'))
        print("***Number of Rows:", len(reviews_df))
        print()

        """ Treat missing values in the Rating and ReviewText variables. 
        In this case, dropna has been chosen as the strategy.   """
        reviews_df.dropna(subset=['Rating', 'ReviewText'], inplace=True)
        print("***Number of Rows:", len(reviews_df))
        print()

        """ Select only the 'ReviewText',  'Rating', 'DivisionName',
         'DepartmentName', and 'ClassName' variables that would matter to the analysis. 
         Creating a new DataFrame called reviews_sub. """
        reviews_df = reviews_df[['Title', 'ReviewText', 'Rating', 'DivisionName', 'DepartmentName', 'ClassName']]

        print(reviews_df)
        print()

        return reviews_df

    def analyseRating(self):
        """Displaying the frequency of rating using a histogram"""

        fig = px.histogram(self.reviews_all, x="Rating")
        fig.update_traces(marker_color='#d57f0e',
                          marker_line_color='rgb(80,15,11)',
                          marker_line_width=1.5)
        fig.update_layout(title_text='Rating Frequency')
        fig.show()

    def analyzeSentiments(self):
        self.reviews_all['sentiment'] = ['positive' if rating > 3 else
                                         'negative' if rating < 3
                                         else 'neutral'
                                         for rating in self.reviews_all['Rating']]
        self.generate_special_word_clouds('all')
        self.generate_special_word_clouds('positive')
        self.generate_special_word_clouds('negative')

    def generate_special_word_clouds(self, sentimentType='all'):
        corpus_txt = ""
        if (sentimentType.lower() == 'all'):
            corpus_txt = " ".join(x for x in self.reviews_all['ReviewText'])
        else:
            reviews_all_sub = self.reviews_all[self.reviews_all['sentiment'] == sentimentType]
            corpus_txt = " ".join(x for x in reviews_all_sub['ReviewText'])

        frequencyDict = self.calculate_word_frequencies(corpus_txt, False, True)

        fileName = ""
        match sentimentType.lower():
            case 'all':
                fileName = "D:\\AllReviews.png"
            case 'positive':
                fileName = "D:\\PosReviews.png"
            case 'negative':
                fileName = "D:\\NegReviews.png"
            case _:
                fileName = "D:\\otherReviews.png"

        self.generateWordCloud(frequencyDict, fileName)

    def generateWordCloud(self, frequencies, path):
        # use this code to generate the word cloud
        cloud = wordcloud.WordCloud()
        cloud.generate_from_frequencies(frequencies)

        cloud.to_file(path)
        print("FILE GENERATED:", path)

        import matplotlib.pyplot as plt
        plt.interactive(True)
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis('off')

        plt.title('Word Cloud: ' + path,
                  fontweight="bold")
        plt.show()

    def calculate_word_frequencies(self, text, stemmed=False, withoutStopWords=False):
        tokens = []
        if stemmed:
            tokens = self.tokenize_withstemming(text)
        else:
            tokens = self.tokenize(text)

        final_tokens = []
        if withoutStopWords:
            final_tokens = self.remove_stopwords(tokens)
        else:
            final_tokens = tokens

        tkn_count_dict = self.get_token_counts(final_tokens)
        return tkn_count_dict

    def remove_stopwords(self, token_list):
        tokensFiltered = [token for token in token_list if token not in self.stopWords]
        return tokensFiltered

    def get_token_counts(self, token_list):
        token_counter = collections.Counter([txt.lower() for txt in token_list])
        return dict(sorted(token_counter.items(), key=lambda item: item[1], reverse=True))

    def getStopWords(self):
        nltk.download('stopwords')
        sWords = set(stopwords.words('english'))
        sWords.update({'would', 'could', 'should', 'i', 'we', 'she', 'he', 'it'})
        print("###### STOP WORDS ######")
        print(sWords, "\n###############\n")
        return sWords

    def tokenize_withstemming(self, doc):
        tokens = self.tokenize(doc)

        # Stemming
        porterstem = stem.PorterStemmer()
        stemTokens = [porterstem.stem(x) for x in tokens]

        return stemTokens

    def tokenize(self, doc):
        text = doc.lower().strip()
        text = re.sub(f'[{string.punctuation}]', " ", text)
        tokens = re.findall(r'\b\w+\b', text)

        return tokens


crp1 = ClothingReviewProject()
crp1.run_project_wrok()
