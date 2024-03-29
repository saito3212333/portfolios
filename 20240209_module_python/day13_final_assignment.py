
import collections
import copy
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
        # self.analyseRating()
        self.stopWords = self.getStopWords()
        # self.analyzeSentiments()
        self.runTextPredictions()


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

        print(reviews_df.head())
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
        self.generate_special_word_clouds( 'all')
        self.generate_special_word_clouds( 'positive')
        self.generate_special_word_clouds( 'negative')

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
    # 入力ドキュメントをトークン化し、次にポーターステミングアルゴリズムを使用して
    # 各トークンにステミングを適用し、ステミングされたトークンのリストを返します。
    # ステミング（stemming）は、自然言語処理において、
    # 単語の語幹（または「基本形」）を抽出するプロセスです。
    # 言語学的に言えば、語幹は単語の形態変化の中で変化しない部分であり、単語の意味を保持する核心部分です。

    #　要するに、バラバラにしてあげて（トークン化）、ステミング（根本の意味に戻す）

    def tokenize(self, doc):
        text = doc.lower().strip()
        text = re.sub(f'[{string.punctuation}]', " ", text)
        tokens = re.findall(r'\b\w+\b', text)

        return tokens

    def remove_punc_stopwords(self, text):
        text_tokens = self.tokenize(text)
        text_tokens = self.remove_stopwords(text_tokens)
        return " ".join(text_tokens)

    def runTextPredictions(self):
        """ Remove punctuations and stopwords from the text data in ReviewText and Title"""
        self.reviews_all['Title'] = [str(x) for x in self.reviews_all['Title']]
        self.reviews_all['ReviewText'] = [str(x) for x in self.reviews_all['ReviewText']]

        reviews_df = copy.deepcopy(self.reviews_all)

        # The following applies remove_punc_stopwords function to each value in the given column. The result is a column with lower case values
        # that have no punctuations, no stop words,
        reviews_df['Title'] = reviews_df['Title'].apply(self.remove_punc_stopwords)
        reviews_df['ReviewText'] = reviews_df['ReviewText'].apply(self.remove_punc_stopwords)

        """ Add a new variable called sentiment; if Rating is greater than 3, then sentiment = 1, else sentiment = -1 """
        reviews_df['sentiment_value'] = [1 if x >= 3 else -1 for x in reviews_df.Rating]

        """ split the dataset into two: train (85% of the obs.) and test (15% of the obs.)"""
        # reviews_sub_train =  reviews_df.sample(freq=0.85)
        # reviews_sub_test =  reviews_df.sample(freq=0.15)

        reviews_df['random_index'] = [rd.uniform(0, 1) for x in range(len(reviews_df))]

        reviews_sub_train = reviews_df[reviews_df.random_index < 0.85][
            ['ReviewText', 'Rating', 'Title', 'sentiment_value']]
        reviews_sub_test = reviews_df[reviews_df.random_index >= 0.85][
            ['ReviewText', 'Rating', 'Title', 'sentiment_value']]

        print(reviews_sub_train.head())
        print(reviews_sub_test.head())

        """ OPTION 3 for retrieving train and test sets.
        from sklearn.model_selection import train_test_split
        reviews_sub_train, reviews_sub_test = train_test_split(reviews_df, test_size=0.15)
        """

        """ count vectorizer:
        Next, we will use a count vectorizer from the Scikit-learn library. This will transform the text in our dataframe 
        into a 'bag of words' model, which will contain a sparse matrix of integers. 

        The number of occurrences of each word will be counted and printed.
        We will need to convert the text into a bag-of-words model since the logistic regression 

        algorithm cannot understand text.

        The bag-of-words model is a popular technique in natural language processing (NLP) 
        for representing text data as numerical vectors. It is a simple and intuitive approach 
        that disregards the order and structure of words in a document and focuses solely on their 
        occurrence frequencies.

        """

        # vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
        vectorizer = TfidfVectorizer(token_pattern=r'\b\w+\b')
        train_matrix = vectorizer.fit_transform(reviews_sub_train['Title'])
        test_matrix = vectorizer.transform(reviews_sub_test['Title'])

        """ 
        print(train_matrix)
        print()
        print()
        print(test_matrix)
        """

        """Perform Logistic Regression"""
        lr = LogisticRegression()

        X_train = train_matrix
        print(X_train.head())
        X_test = test_matrix
        y_train = reviews_sub_train['sentiment_value']
        y_test = reviews_sub_test['sentiment_value']

        lr.fit(X_train, y_train)
        print("Coefficients:")
        print(lr.coef_)
        print("Intercept:")
        print(lr.intercept_)

        print()
        """ Generate the predictions for the test dataset"""
        predictions = lr.predict(X_test)
        reviews_sub_test['predictions'] = predictions
        print(reviews_sub_test.head(30))

        print()
        """Calculate the prediction accuracy"""
        reviews_sub_test['match'] = reviews_sub_test['sentiment_value'] == reviews_sub_test['predictions']

        print("")
        print("Prediction Accuracy:")
        print(sum(reviews_sub_test['match']) / len(reviews_sub_test))

        ## Multinomial Logisitic Regression Model
        lr2 = LogisticRegression()

        X_train = train_matrix
        X_test = test_matrix
        y_train2 = reviews_sub_train['Rating']
        y_test2 = reviews_sub_test['Rating']

        lr2.fit(X_train, y_train2)
        print(lr2)

        """ Generate the predictions for the test dataset"""
        predictions2 = lr2.predict(X_test)
        reviews_sub_test['predictions_rating'] = predictions2
        print(reviews_sub_test.head(30))

        reviews_sub_test['match_rating'] = reviews_sub_test['Rating'] == reviews_sub_test['predictions_rating']

        print("")
        print("Prediction Accuracy:")
        print(sum(reviews_sub_test['match_rating']) / len(reviews_sub_test))

crp1 = ClothingReviewProject()
#crp1.run_project_wrok()
t = '''Athens, Greece
CNN
 — 
The Greek parliament on Thursday passed a law legalizing same-sex marriage, in a landmark victory for human rights in Greece and making it the first majority Orthodox Christian country to establish marriage equality for all.

This is a breaking news story. More details to come.

RELATED

'''
print(crp1.tokenize_withstemming(t))
print(crp1.tokenize(t))