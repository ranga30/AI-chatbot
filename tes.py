from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings
warnings.filterwarnings('ignore')
nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)
article=Article('https://en.wikipedia.org/wiki/Chronic_condition')
article.download()
article.parse()
article.nlp()
corpus=article.text
text=corpus
sent_tokens=nltk.sent_tokenize(text)
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)

def LemNormalize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

Greeting=["hi","hello","hola","greetings","wassup","hey"]
gr=["howdy","hi","hey there"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in Greeting:
             return random.choice(Greeting)
def response(user_re):


    user_re=user_re.lower()
    print(user_re)
    robo_re=''
    sent_tokens.append(user_re)
    Tfidvec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
    tfidf=Tfidvec.fit_transform(sent_tokens)

    vals=cosine_similarity(tfidf[-1],tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten()
    flat.sort()
    score=flat[-2]hol
    if(score==0):
        robo_re=robo_re+"I apologize, i dont understand."
    else:
        robo_re=robo_re+sent_tokens[idx]

    sent_tokens.remove(user_re)
    return robo_re
flag=True
print("STONER: Iam STONER here to assist you")
while(flag==True):
    user_re=input()
    user_re=user_re.lower()
    if(user_re!='bye'):
        if(user_re=='thanks' or user_re=="thank you"):
            flag=False
            print("STONER: You are welcome")
        else:
            if(greeting(user_re)!=None):
                print("STONER :"+greeting(user_re))
            else:
                print("STONER:"+response(user_re))

    else:
        flag=False
        print("STONER:Chat with you later!")