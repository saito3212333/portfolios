import pandas as pd
import collections
import copy
import re
import string
import random as rd
import nltk
from nltk import stem
from nltk.corpus import stopwords
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from wordcloud import wordcloud


# defining the class
class FinalPrjEngine:
    # initialize
    books = pd.DataFrame()
    book_ratings = pd.DataFrame()
    reviews = pd.DataFrame()
    stopWords = []

    def executeTasks(self):
        # loading source data into data frames
        # self.loadData()
        #
        # # performing initial sanity checks
        # self.reviews = self.performSanityChecks()

        # # # Generating initial analytical visualizations to understand the reviews
        # self.visualize()
        #
        # # get stopWords
        # self.stopWords = self.getStopWords()
        #
        # # Classifing reviews into two ‘sentiment’ categories called positive and negative
        # self.classifyReviews()

        self.runTextPredictions()

    def loadData(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        # loading source data into data frames
        self.books = pd.read_csv("./Data/books_data.csv")
        self.book_ratings = pd.read_csv('./Data/Books_rating.csv')


    # performing initial sanity checks
    def performSanityChecks(self):
        # look at the first rows in the dfs to understand the data and structure
        # print('### head ###')
        # print(self.books.head(3))
        # print(self.book_ratings.head(3))
        #
        # # Summarizing statistics for the columns
        # print('### describe ###')
        # print(self.books.describe(include='all'))
        # print(self.book_ratings.describe(include='all'))
        #
        # # column name, non-null count, dataType and #of entries
        # print('### info ###')
        # print(self.books.info())
        # print(self.book_ratings.info())

        # merging the dataframes
        # Select only the variables that would matter to the analysis
        merged_df = pd.merge(
            self.book_ratings[['Id', 'Title', 'Price', 'review/score', 'review/summary', 'review/text']],
            self.books[['Title', 'categories', 'ratingsCount']],
            on='Title', how='left')
        # updating column names
        merged_df.columns = ['Id', 'Title', 'Price', 'reviewScore', 'reviewSummary', 'reviewText', 'categories',
                             'ratingsCount']

        print('### merged_df ###')
        #####print(merged_df.describe(include='all'))
        print('Number of rows:', len(merged_df))
        print('Number of duplicated:', merged_df.duplicated().sum()) ## Kazuki what if we add this code for making sure the no of duplicates?
        # duplicate handling
        # remove the duplicate rows from merged_df
        # exactly same rows are assumed as duplicate
        # keep: first (default value), inplace: True (replaces the source dataframe), ignore_index: false (default value)
        merged_df.drop_duplicates(inplace=True)
        print('Number of rows after dropping duplicates:', len(merged_df))

        # Check for missing values
        print('### missing values for merged_df ###')
        print(
            merged_df.isnull().sum())  # 207 rows without Title, 8 rows without reviewText, 407 rows without reviewSummary
        # Treat missing values
        # delete the records either title or reviewScore or reviewText has missing values
        # (reviews without Title has no meaning this is why also dropping empty titles)
        merged_df.dropna(subset=['Title', 'reviewScore', 'reviewText', 'reviewSummary'], inplace=True)
        print("### number of rows after dropping nas:", len(merged_df))

        # delete books and book_ratings from memory
        del self.books
        del self.book_ratings

        merged_df.to_csv('merged_df.csv', index=False)
        return merged_df

    # Generating initial analytical visualizations to understand the reviews
    def visualize(self):
        # adding price categ field to see the impact of price on reviewScore
        Q1 = self.reviews['Price'].quantile(0.25)
        Q3 = self.reviews['Price'].quantile(0.75)
        IQR = Q3 - Q1
        # Define the price ranges and labels for price categories
        bins = [Q1 - 1.5 * IQR, self.reviews['Price'].quantile(0.40), self.reviews['Price'].quantile(0.60),
                Q3 + 1.5 * IQR, float('inf')]
        labels = ['Low', 'Medium', 'High', 'Very High']
        # Add priceCateg based on the 'Price
        self.reviews['priceCateg'] = pd.cut(self.reviews['Price'], bins=bins, labels=labels, right=False)

        # Displaying the distribution of ratings across different price categories
        fig = px.histogram(self.reviews, x="reviewScore", color='priceCateg',
                           color_discrete_map={'Low': 'rgb(57,172,231)', 'Medium': 'rgb(155,212,228)',
                                               'High': 'rgb(7,132,181)', 'Very High': 'silver'},
                           title='Histogram of Review Scores by Price Category',
                           labels={'reviewScore': 'Review Score', 'priceCateg': 'Price Category'}
                           )
        fig.update_layout(width=800, height=600)
        fig.show()

        fig2 = px.scatter(self.reviews, x='Price', y='reviewScore',
                          title='Relationship between Price and Review Score',
                          labels={'Price': 'Price', 'reviewScore': 'Review Score'})
        fig2.update_layout(width=800, height=600)
        fig2.show()



        # グラフの表示
        fig.show()


    def getStopWords(self):
        nltk.download('stopwords')
        sWords = set(stopwords.words('english'))
        sWords.update({'would', 'could', 'should', 'i', 'we', 'she', 'he', 'it'})
        print("###### stop words ######")
        print(sWords, "\n###############\n")
        return sWords

    # Classifing reviews into two ‘sentiment’ categories called positive and negative
    def classifyReviews(self):
        self.reviews['sentiment'] = ['positive' if reviewScore > 3 else
                                     'negative' if reviewScore < 3
                                     else 'neutral'
                                     for reviewScore in self.reviews['reviewScore']]

        # # generate word clouds without stemming for reviewSummary
        # self.generate_special_word_clouds('all',False, 'reviewSummary')
        # self.generate_special_word_clouds('positive', False, 'reviewSummary')
        # self.generate_special_word_clouds('negative', False, 'reviewSummary')
        # # generate word clouds with stemming for reviewSummary
        # self.generate_special_word_clouds('all',True, 'reviewSummary')
        # self.generate_special_word_clouds('positive',True, 'reviewSummary')
        # self.generate_special_word_clouds('negative',True, 'reviewSummary')
        #
        # # generate word clouds without stemming for reviewText
        # self.generate_special_word_clouds('all',False, 'reviewText')
        # self.generate_special_word_clouds('positive',False, 'reviewText')
        # self.generate_special_word_clouds('negative',False, 'reviewText')
        # # generate word clouds with stemming  for reviewText
        # self.generate_special_word_clouds('all',True, 'reviewText')
        # self.generate_special_word_clouds('positive',True, 'reviewText')
        # self.generate_special_word_clouds('negative',True, 'reviewText')

    # Generating word clouds
    # based on the specified sentiment type and text column
    def generate_special_word_clouds(self, sentimentType='all', stmmd=False, textCol='reviewSummary'):
        # for reviewText; generate random sample of data and work on it
        # (data is huge when try to process all for reviewText, it is getting memory error, this is why we used sample here)
        if textCol == 'reviewText':
            dataSet = self.generateSample()
        else:
            dataSet = self.reviews

        # Extract the text data based on the specified sentiment type
        corpus_txt = ""
        if (sentimentType.lower() == 'all'):
            corpus_txt = " ".join(str(x) for x in dataSet[textCol])
        else:
            reviews_sub = dataSet[dataSet['sentiment'] == sentimentType]
            corpus_txt = " ".join(str(x) for x in reviews_sub[textCol])

        # Calculate word frequencies for the corpus text
        frequencyDict = self.calculate_word_frequencies(corpus_txt, stmmd, True)

        # Define the file name for saving the word cloud image
        fileName = ""
        if stmmd:
            fileName = "./Data/" + sentimentType + "_" + textCol + "stemmed.png"
        else:
            fileName = "./Data/" + sentimentType + "_" + textCol + ".png"

        # Generate the word cloud image and save it to the specified file
        self.generateWordCloud(frequencyDict, fileName)

    # Generate a word cloud from the given word frequencies and save it to the specified path
    def generateWordCloud(self, frequencies, path):
        # generating the word cloud object
        cloud = wordcloud.WordCloud()
        cloud.generate_from_frequencies(frequencies)

        # Save the generated word cloud to the specified path
        cloud.to_file(path)
        print("FILE GENERATED:", path)

        import matplotlib.pyplot as plt
        plt.interactive(True)
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis('off')

        plt.title('Word Cloud: ' + path, fontweight="bold")
        plt.show()

    # Calculate the word frequencies in the given text return a dictionary with tokens and frequencies
    def calculate_word_frequencies(self, text, stemmed=False, withoutStopWords=False):
        # tokenize text (with or without stemming)
        tokens = []
        if stemmed:
            tokens = self.tokenize_withstemming(text)
        else:
            tokens = self.tokenize(text)

        # Remove stopwords if specified
        final_tokens = []
        if withoutStopWords:
            final_tokens = self.remove_stopwords(tokens)
        else:
            final_tokens = tokens

        tkn_count_dict = self.get_token_counts(final_tokens)
        return tkn_count_dict

    # remove stop words
    def remove_stopwords(self, token_list):
        tokensFiltered = [token for token in token_list if token not in self.stopWords]
        return tokensFiltered

    '''Count the occurrences of each token in token_list and return a dictionary
          with tokens as keys and counts; sorted in descending order of frequency'''

    def get_token_counts(self, token_list):
        token_counter = collections.Counter([txt.lower() for txt in token_list])
        return dict(sorted(token_counter.items(), key=lambda item: item[1], reverse=True))

    # tokenize with stemming
    def tokenize_withstemming(self, doc):
        tokens = self.tokenize(doc)

        # Stemming
        porterstem = stem.PorterStemmer()
        stemTokens = [porterstem.stem(x) for x in tokens]

        return stemTokens

    # splitting doc to tokens
    def tokenize(self, doc):
        text = doc.lower().strip()
        # removing punctuation
        text = re.sub(f'[{string.punctuation}]', " ", text)
        tokens = re.findall(r'\b\w+\b', text)
        return tokens

    def generateSample(self):
        # generate random sample from the data
        self.reviews['random_index'] = [rd.uniform(0, 1) for x in range(len(self.reviews))]

        reviews_sample = self.reviews[self.reviews.random_index < 0.3][
            ['Id', 'Title', 'reviewScore', 'reviewSummary', 'reviewText', 'sentiment']]

        return reviews_sample



    def runTextPredictions(self):
        merged_df = pd.read_csv('merged_df.csv')
        merged_df['random_index'] = [rd.uniform(0, 1) for x in range(len(merged_df))]
        merged_df = merged_df.sample(8000)

        reviews_sub_train = merged_df[merged_df.random_index < 0.85][
            ['reviewText', 'reviewScore']]
        reviews_sub_test = merged_df[merged_df.random_index >= 0.85][
            ['reviewText', 'reviewScore', 'Title']]

        print(reviews_sub_train.head())
        print(reviews_sub_test.head())


        # vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
        vectorizer = TfidfVectorizer(token_pattern=r'\b\w+\b')
        train_matrix = vectorizer.fit_transform(reviews_sub_train['reviewText'])
        test_matrix = vectorizer.transform(reviews_sub_test['reviewText'])


        ## Multinomial Logisitic Regression Model
        lr2 = LogisticRegression()

        X_train = train_matrix
        X_test = test_matrix
        y_train2 = reviews_sub_train['reviewScore']
        y_test2 = reviews_sub_test['reviewScore']

        lr2.fit(X_train, y_train2)
        print(lr2)

        """ Generate the predictions for the test dataset"""
        predictions2 = lr2.predict(X_test)
        reviews_sub_test['predictions_score'] = predictions2
        print(reviews_sub_test.head(30))

        reviews_sub_test['match_score'] = reviews_sub_test['reviewScore'] == reviews_sub_test['predictions_score']

        print("")
        print("Prediction Accuracy:")
        print(sum(reviews_sub_test['match_score']) / len(reviews_sub_test))
        # output 0.6275805119735756



# creating an instance of the class
fpe1 = FinalPrjEngine()
# executing project tasks
fpe1.executeTasks()