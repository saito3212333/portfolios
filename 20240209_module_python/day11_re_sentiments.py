import re
import string
import requests


class ReEngine2:
    def do_ex1(self):
        """
        r'[a-zA-Z0-9]+' :: Searching for any number of alphanumeric characters excluding _.
        r'\d' :: Searching for ONE numeric digit.
        r'\d\d' :: Searching for TWO numeric digits.
        r'\d*.\d{3}' :: Searching zero or more digits followed by any charadcter and THREE digits. 45h134 / y783 / 73824$342 / *342
        r'\d{11}' :: Searching for 11 numeric digits.  83746372817 / 48287390243 / 00000000000 / 11111111111
        r'[a-z0-9\.@#$%&]+' :: Searching for ONE or MORE lowercase alphas, digits,
                            or the following special characters: . @ # $ % &.
        r'[a-zA-Z0-9\s]{6,20}'  :: Searching for any alphanumeric or whitespace characters, excluding _, 6 to 20 times.
        r'https:/{2}[\w.]+[.]com' ::  'https://happyday.com', 'https://apple.picking.com'
        r'</?[\w\s]*>|<.+[\W]>' :: tags in an html context <div> </div> <span>
        r'(.+)/([^/]+)' :: k/ha   D:/tsom/da
        r'[\w,\s-]+\.[A-Za-z]{3}' :: hads.com     people.net
        """

        # r'[a-zA-Z0-9]+': アンダースコアを除く、英数字の1文字以上の連続を検索します。
        # r'\d': 1つの数字を検索します。
        # r'\d\d': 2つの数字を検索します。
        # r'\d*.\d{3}': 0個以上の数字の後に任意の文字、そして3つの数字を検索します。
        # 例：45h134 / y783 / 73824$342 / *342
        # r'\d{11}': 11桁の数字を検索します。
        # 例：83746372817 / 48287390243 / 00000000000 / 11111111111
        # r'[a-z0-9\.@#$%&]+': 小文字のアルファベット、数字、または次の特殊文字のいずれか（. @ # $ % &）を1文字以上検索します。
        # r'[a-zA-Z0-9\s]{6,20}': アンダースコアを除く、英数字または空白の文字が6から20回連続しているものを検索します。
        # r'https:/{2}[\w.]+[.]com': "https://happyday.com"や"https://apple.picking.com"のような.comドメインを含むURLを検索します。
        # r'</?[\w\s]*>|<.+[\W]>': HTMLコンテキスト内のタグを検索します。
        # 例：<div> </div> <span>
        # r'(.+)/([^/]+)': スラッシュで区切られた2つの要素を抽出します。
        # 例：k/ha D:/tsom/da
        # r'[\w,\s-]+\.[A-Za-z]{3}': 3文字の拡張子を持つファイル名を検索します。
        # 例：hads.com people.net

        str2 = "hey you, how are you? ba ba black sheep had a lot of whool. \\you are good.\\ &^%, fly a k&$#!"
        print()
        result1 = re.findall(r'[a-z0-9.@#$%&]+', str2, re.I)
        print(result1)

        print()
        # \\　スラッシュを検索対象に入れるかどうかの違いです。
        result1 = re.findall(r'[a-z0-9\\.@#$%&]+', str2, re.I)
        print(result1)

        str2 = "hey you, how are you? https://happyday.com https://apple.picking.com https://big.bang.ca"
        print()
        result1 = re.findall(r'https:/{2}[\w.]+[.]com', str2, re.I)
        print(result1)

    def do_ex2(self):
        with open("./data/email.txt") as f:
            email = f.read()
        """ 
        List all the email addresses
        List all the phone numbers
        Extract the subject
        Extract the summary of reasons
        """
        print("EX 2")
        print(email)

        print()
        email_addresses = set(re.findall(r"\b\S+[@][\w.]+\b", email, re.I))
        print(email_addresses)
        # re.findall(r"\b\S+[@][\w.]+\b", email, re.I):
        # このパターンは、電子メールアドレスを抽出します。以下の要素が含まれます:
        #
        # \b: 単語の境界を表します。
        # \S+: 空白以外の文字が1つ以上続くことを表します。
        # [@]: @マークを表します。
        # [\w.]+: ドメイン部分の文字列を表します。これには、英数字とピリオドが含まれます。
        # \b: 単語の境界を表します。
        # re.I: 大文字小文字を区別せずに検索します。
        # re.findall(r"[+]?[0-9 ]+\d", email, re.I):

        print()
        phone_numbers = set(re.findall(r"[+]?[0-9 ]+\d", email, re.I))
        print(phone_numbers)

        # このパターンは、電話番号を抽出します。以下の要素が含まれます:
        #
        # [+]?: "+"文字が0回または1回現れることを表します。
        # [0-9 ]+: 数字とスペースが1つ以上連続することを表します。
        # \d: 数字を表します。
        # re.I: 大文字小文字を区別せずに検索します。
        # Extract
        # the subject


        print('Look for the subject?')
        subject = re.findall(r'Subject: .+[!]', email, re.I)
        print(subject)
        # re.findall(r'Subject: .+[!]', email, re.I):
        # このパターンは、電子メールの件名を抽出します。以下の要素が含まれます：
        #
        # Subject: : "Subject: " という文字列を表します。
        # .+: 任意の文字が1つ以上続くことを表します。
        # [!]: "!" という文字を表します。
        # re.I: 大文字小文字を区別せずに検索します。
        # re.split(r'reasons:', email, re.I):

        # Extract the summary of reasons
        print("Look for the summary of reasons?")
        parts = re.split(r'reasons:', email, re.I)
        print(parts)
        reasons = re.findall(r'[^:\n]+:\s', parts[1], re.I)
        print(reasons)
        #     # このパターンは、電子メールの本文から "reasons:" という文字列を基準に分割します。以下の要素が含まれます：
        #         #
        #         # reasons:: "reasons:" という文字列を表します。
        #         # re.I: 大文字小文字を区別せずに検索します。
        #         # re.findall(r'[^:\n]+:\s', parts[1], re.I):
        #         # このパターンは、"reasons:" の後に続く要約情報を抽出します。以下の要素が含まれます：
        #         #
        #         # [^:\n]+: コロン (":") や改行文字 ("\n") を除く任意の文字が1つ以上続くことを表します。
        #         # :\s: コロンとスペースを表します。
        #         # re.I: 大文字小文字を区別せずに検索します。

    def demonstrateRE(self):
        txt = "An arbitrary number of REs can be separated by the '|' in this way."
        x = re.search("\w*(ar)\w*", txt)
        print(x)#<_sre.SRE_Match object; span=(3, 12), match='arbitrary'>
        print(x.span())
        print(x.string)
        print(x.group())
        # print(x.span()): マッチした部分文字列の開始と終了のインデックスを出力します。
        # print(x.string): re.search に渡された文字列を出力します。
        # print(x.group()): マッチした部分文字列を出力します。

        print()
        txt = "An arbitrary number of REs can be separated by the '|' in this way."
        x = re.split(f"\s[{string.punctuation}]*\|[{string.punctuation}]*\s", txt)
        print(x)
        # re.split(f"\s[{string.punctuation}]*\|[{string.punctuation}]*\s", txt):
        # 文字列 txt を定義されたパターンで分割します。
        # ここでは、オプションの空白と句読点文字に囲まれた "|" が見つかるたびに文字列が分割されます。
        # print(x): 文字列を分割した後の結果のリストを出力します。


        print()
        # Replace all white-space characters with the digit ";":
        txt = "There is a a key to solve every porblem."

        #  \s は　空白ね！　お忘れなく。
        x = re.sub("\s", ";", txt)
        print(x)
        # 正規表現の使用:
        #
        # re.sub() は正規表現を使用してパターンを指定し、文字列内のパターンに一致する部分を置換します。
        # str.replace() は単純な文字列を検索して置換します。正規表現ではなく、指定された文字列をそのまま検索して置換します。
        # 柔軟性:
        #
        # re.sub() は複雑なパターンに一致する部分を置換できるため、より柔軟です。例えば、空白文字全体を置換するのではなく、特定の条件を持つ空白文字のみを置換することができます。
        # str.replace() は文字列の完全な一致のみを置換します。より複雑なパターンに一致する部分を置換することはできません。
        # パフォーマンス:
        #
        # str.replace() は単純な文字列操作であり、正規表現エンジンを使用しないため、通常は高速です。
        # re.sub() は正規表現エンジンを使用してパターンマッチングを行うため、文字列が大きくなると性能が低下する可能性があります。
        # したがって、置換に正規表現が必要であれば re.sub() を使用し、単純な文字列の置換で十分であれば str.replace() を使用します

        # 簡単にいうと、subは複雑なことができるよ。!!!!!

        print()
        # with open("tsom.html") as f:
        #     str3 = f.read()
        #
        # print(str3)
        # result1 = set(re.findall(r"https:/{2}[\w./\\\-$%]+", str3, re.I))
        # print(result1)
        # print()
        # print("\n".join(result1))

a = ReEngine2()
#.do_ex1()
#a.do_ex2()
a.demonstrateRE()