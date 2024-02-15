import collections
import re
import string
import urllib.request

import nltk
import numpy as np
import wordcloud
from nltk import stem
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer

class InformationRetrievalEngine:
    sms_corpus = []
    stopWords = []
    
    def __init__(self):
        with urllib.request.urlopen("https://storage.googleapis.com/wd13/SMSSpamCollection.txt") as url:
            for line in url.readlines():
                # print(type(line))
                self.sms_corpus.append(line.decode().split('\t'))

        self.getStopWords()
    
    
    def demonstrateIR(self):
        # print the text and label of document 16
        docid = 16
        print(self.sms_corpus[docid])
        # print the label of document 16
        print( self.sms_corpus[docid][0])
        # print the text of document 16
        print( self.sms_corpus[docid][1])

        print()
        # print the text and label of document 16
        docid = 20
        print( self.sms_corpus[docid])
        # print the label of document 16
        print( self.sms_corpus[docid][0])
        # print the text of document 16
        print( self.sms_corpus[docid][1])

        print()
        doc25_msg =  self.sms_corpus[25][1]
        print(doc25_msg)
        print(self.tokenize(doc25_msg))

    def tokenize(self, doc):
        text = doc.lower().strip()
        text = re.sub(f'[{string.punctuation}]', " ", text)
        tokens = re.findall(r'\b\w+\b', text)

        return tokens

    def get_token_counts(self,token_list):
        token_counter = collections.Counter([txt.lower() for txt in token_list])
        return dict(sorted(token_counter.items(), key=lambda item: item[1], reverse=True))

    def search_by_bir(self, keywords):
        # sms_corpus = [ [label, msg], [label, msg], [label, msg],.... ]

        search_pat = "|".join(keywords)

        result_dict = {indx: val for indx, val in enumerate( self.sms_corpus) if re.search(search_pat, val[1]) != None}

        # for i in range(len( self.sms_corpus)):
        #     if (re.search(search_pat,  self.sms_corpus[i][1]) != None):
        #         result_dict[str(i)] =  self.sms_corpus[i]

        """
        { 17 : ['ham','ha ha ... you got me...'],
            25 : ['ham','Do you love me?']
        }
        """
        return result_dict

    def calculate_sms_word_frequencies(self, type='all'):
        selected_msgs = []
        match type.lower():
            case 'all':
                selected_msgs = self.sms_corpus
            case 'ham':
                selected_msgs = [msg for msg in self.sms_corpus if msg[0] == 'ham']
            case 'spam':
                selected_msgs = [msg for msg in self.sms_corpus if msg[0] == 'spam']
            case _:
                selected_msgs = self.sms_corpus

        msgs_text = [msg[1] for msg in selected_msgs]
        text = " ".join(msgs_text)
        tockens = self.tokenize(text)
        tkn_count_dict = self.get_token_counts(tockens)
        return tkn_count_dict

    def calculate_sms_word_frequencies2(self, type='all', stemmed=False, withoutStopWords=False):
        selected_msgs = []
        match type.lower():
            case 'all':
                selected_msgs = self.sms_corpus
            case 'ham':
                selected_msgs = [msg for msg in self.sms_corpus if msg[0] == 'ham']
            case 'spam':
                selected_msgs = [msg for msg in self.sms_corpus if msg[0] == 'spam']
            case _:
                selected_msgs = self.sms_corpus

        msgs_text = [msg[1] for msg in selected_msgs]
        text = " ".join(msgs_text)
        return self.calculate_word_frequencies(text,stemmed,withoutStopWords)

    def do_ex_1(self):
        print("### ALL WORDS ####")
        print(self.calculate_sms_word_frequencies('all'))
        print()
        print("### HAM WORDS ####")
        print(self.calculate_sms_word_frequencies('ham'))
        print()
        print("### SPAM WORDS ####")
        print(self.calculate_sms_word_frequencies('spam'))

        print()
        print()
        print("### ALL WORDS ####")
        print(self.calculate_sms_word_frequencies2('all', False, True))
        print()
        print("### HAM WORDS ####")
        print(self.calculate_sms_word_frequencies2('ham', False, True))
        print()
        print("### SPAM WORDS ####")
        print(self.calculate_sms_word_frequencies2('spam', False, True))

    def demonstrateBIR(self):
        print(self.search_by_bir(['Arabian']))
        print()
        print(self.search_by_bir(['sweet']))

    def getStopWords(self):
        nltk.download('stopwords')
        self.stopWords = list(set(stopwords.words('english')))
        print(self.stopWords)
        return self.stopWords

    def remove_stopwords(self, token_list):
        tokensFiltered = [token for token in token_list if token not in self.stopWords]
        return tokensFiltered

    def tokenize_withstemming(self, doc ) :
        tokens = self.tokenize(doc)

        # Stemming
        porterstem = stem.PorterStemmer()
        stemTokens = [porterstem.stem(x) for x in tokens]

        return stemTokens

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

    def demonstrateTDIF(self):
        corpus = [
            'This is the first document.',
            'This document is the second document.',
            'And this is the third one.',
            'Is this the first document?']

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(corpus)

        vectorizer.get_feature_names_out()

        print()
        print(X.shape)
        print()
        print(dir(vectorizer))
        print()
        print(corpus)
        print(X)

        all_feature_name = vectorizer.get_feature_names_out()
        print()
        for word in all_feature_name:
            # index in the vocabulary
            indx=vectorizer.vocabulary_.get(word)
            idf_score=vectorizer.idf_[indx]
            print(f"{indx} - {word} : {idf_score}" )

        print()
        corpus2 = [
            'Today is a special day.',
            'For today to be today, today needs to be special.',
            'How do you like today?',
            'special day like today are not actually special.']

        vectorizer2 = TfidfVectorizer()
        trans_2 = vectorizer2.fit_transform(corpus2)

        print(corpus2)
        print(trans_2)


        all_feature_name = vectorizer2.get_feature_names_out()
        print()
        for word in all_feature_name:
            # index in the vocabulary
            indx = vectorizer2.vocabulary_.get(word)
            idf_score = vectorizer2.idf_[indx]
            print(f"{indx} - {word} : {idf_score}")

        def get_vocab_index(word, vecotroizer):
            return vecotroizer.vocabulary_.get(word)

        print()
        print(trans_2[:, get_vocab_index('special', vectorizer2)])

        print()
        print(trans_2[:, get_vocab_index('needs', vectorizer2)])

        print()
        print(trans_2[:, get_vocab_index('today', vectorizer2)])

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

    def generateSMSWordClouds(self):
        # Frequency and wordcloud for all SMSs
        freq_all = self.calculate_sms_word_frequencies2('all', False, False)
        print(freq_all)
        self.generateWordCloud(freq_all, "D:\\sms_all_noStemming_withStops.png")

        # Frequency and wordcloud for all SMSs
        freq_all = self.calculate_sms_word_frequencies2('all', False, True)
        print(freq_all)
        self.generateWordCloud(freq_all, "D:\\sms_all_noStemming_noStops.png")


        freq_all = self.calculate_sms_word_frequencies2('spam', False, True)
        print(freq_all)
        self.generateWordCloud(freq_all, "D:\\sms_SPAM_noStemming_noStops.png")

        freq_all = self.calculate_sms_word_frequencies2('ham', False, True)
        print(freq_all)
        self.generateWordCloud(freq_all, "D:\\sms_HAM_noStemming_noStops.png")


ire1 = InformationRetrievalEngine()
#ire1.demonstrateIR()
#ire1.do_ex_1()
#ire1.demonstrateBIR()
#ire1.demonstrateTDIF()
ire1.generateSMSWordClouds()