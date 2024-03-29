import collections




#
# You may only use str and string methods/functions, in-built lists, and in-built dictionaries.

def create_tolenList(text):
    text = text.strip()
    xWords = text.lower().split()
    xWords = [i.strip() for i in xWords]  # 空白を削除　スプリットされた一文字ずつ
    text2 = ' '.join(xWords)
    text2_lst = list(text2)
    print(text2)
    counter = 0
    for c in text2_lst:
        if not (c.isalnum()):
            text2_lst[counter] = ' '
        counter += 1
    print(text2_lst)
    text3 = ''.join(text2_lst)
    print(text3)
    return text3.split()

def get_token_counts(token_list):
    token_counter = collections.Counter([txt.lower() for txt in token_list])
    print(dict(sorted(token_counter.items(), key=lambda item: item[1], reverse=True)))

tgt = '''
Create a function that takes a multiline string as an input and outputs a list of tokens. It must carry out the following obligations:

Remove the input string's leading and trailing whitespace.
Change all of the string's letters to lowercase.
Use the space character to divide the tokens or words into the original group.
Remove from this list any words that contain special characters or numbers.   
 

Create a second function that uses the list of tokens created by the first one to create a dictionary that counts the frequency with which each token appears.  

Test the functions.

You may only use str and string methods/functions, in-built lists, and in-built dictionaries.  
'''

get_token_counts(create_tolenList(tgt))