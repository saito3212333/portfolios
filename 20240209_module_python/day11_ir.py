import re
import string
import urllib.request


class InformationRetrievalEngine:
    def demonstrateIR(self):
        sms_corpus = []

        with urllib.request.urlopen("https://storage.googleapis.com/wd13/SMSSpamCollection.txt") as url:
            for line in url.readlines():
                sms_corpus.append(line.decode().split('\t'))

        # print the text and label of document 16
        docid = 16
        print(sms_corpus[docid])
        # print the label of document 16
        print(sms_corpus[docid][0])
        # print the text of document 16
        print(sms_corpus[docid][1])

        print()
        # print the text and label of document 16
        docid = 20
        print(sms_corpus[docid])
        # print the label of document 16
        print(sms_corpus[docid][0])
        # print the text of document 16
        print(sms_corpus[docid][1])

        print()
        doc25_msg = sms_corpus[25][1]
        print(doc25_msg)
        print(self.tokenize(doc25_msg))

    def tokenize(self, doc):
        text = doc.lower().strip()
        text = re.sub(f'[{string.punctuation}]', " ", text)
        tokens = re.findall(r'\b\w+\b', text)

        return tokens

ire1 = InformationRetrievalEngine()
ire1.demonstrateIR()