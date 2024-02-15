import re
import string
import requests

# マディーのコードは他のライブラリ使ってたけど、認証の問題で使えなかったので、requestに変更しました。

class InformationRetrievalEngine:
    def demonstrateIR(self):
        sms_corpus = []

        response = requests.get("https://storage.googleapis.com/wd13/SMSSpamCollection.txt")

        for line in response.text.splitlines():
            sms_corpus.append(line.split('\t'))

        # print the text and label of document 16
        docid = 16
        print(12,sms_corpus[docid])
        # 12 ['ham', "Oh k...i'm watching here:)"] これが出力　これの中からまたなんか選べるっぽいな。
        # print the label of document 16
        print(sms_corpus[docid][0])
        # print the text of document 16
        print(sms_corpus[docid][1])

        print()
        # print the text and label of document 20
        docid = 20
        print(sms_corpus[docid])
        # print the label of document 20
        print(sms_corpus[docid][0])
        # print the text of document 20
        print(sms_corpus[docid][1])

        print()
        doc25_msg = sms_corpus[25][1]
        print(doc25_msg)
        print(self.tokenize(doc25_msg))

    def tokenize(self, doc):
        text = doc.lower().strip()
        # re.sub() メソッドを使って、string.punctuation に含まれる句読点をスペースに置換します。
        # 結局どういうこと？
        text = re.sub(f'[{string.punctuation}]', " ", text)
        tokens = re.findall(r'\b\w+\b', text)
        # re.findall() メソッドを使って、正規表現 \b\w+\b にマッチする単語を抽出します。
        # ここで \b は単語の境界を表し、\w+ は1つ以上の単語文字を表します。
        return tokens

ire1 = InformationRetrievalEngine()
ire1.demonstrateIR()
