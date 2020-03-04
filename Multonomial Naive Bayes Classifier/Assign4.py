# Prabhas Kumra
# CS-458
# Assignment-4

import random
import numpy as np
import nltk
from nltk.corpus import movie_reviews
# nltk.download('movie_reviews')

from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
# nltk.download('stopwords')

from nltk.stem import WordNetLemmatizer 
# nltk.download('wordnet')
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


raw_data =[]
training_set = [] 
testing_set = []
training_sentiment = []
X = [] 
Y = []
test_model = []
y_true = []

#1
def build_raw_data():

    
    for category in movie_reviews.categories():
        # print(category)
        for fileid in movie_reviews.fileids(category):
            review_words = movie_reviews.words(fileid)
            review_text = ' '
            for word in review_words:
                review_text += ' ' + word
            review_dictionary = {'text':review_text, 'sentiment': category}
            raw_data.append(review_dictionary)


    stop_words = set(stopwords.words('english')) 

    for i in range(len(raw_data)):
        # print (len(raw_data))
        # print(" ")
        # print (raw_data[i])

        word_tokens = word_tokenize(raw_data[i]['text']) 
        # print(word_tokens)
        # print(raw_data[i]['sentiment'])

        removed_stop_words = [word for word in word_tokens if word not in stop_words]
        # print(removed_stop_words)

        lemmatizer = WordNetLemmatizer() 
        raw_data[i]['text'] = " ".join(lemmatizer.lemmatize(token) for token in removed_stop_words)
        


#2
def feature_selection():

    training_texts = []
    
    for i in range(len(training_set)):
        training_texts.append(training_set[i]['text'])
        # print(training_set[i]['text'])

        if training_set[i]['sentiment'] == 'pos':
            Y.append(1)
        else:
            Y.append(-1)

        
    testing_texts = []
    for i in range(len(testing_set)):
        testing_texts.append(testing_set[i]['text'])

        if testing_set[i]['sentiment'] == 'pos':
            y_true.append(1)
        else:
            y_true.append(-1)

    tfidf = TfidfVectorizer(min_df = 0.01, max_df = 0.6, ngram_range = (1,2))

    tfidfm = tfidf.fit(training_texts)
    X = tfidfm.transform(training_texts)
    X = X.todense()

    test_model = tfidfm.transform(testing_texts)
    test_model = test_model.todense()

    return X, Y, test_model
    
#3
def text_to_vector(list):
    print("text to vector")

#4
def split_data():


    shuffled_numbers = list(range(2000))
    random.Random(20).shuffle(shuffled_numbers)
    counter = 0

    for i in range(1500):
        training_set.append(raw_data[shuffled_numbers[counter]]) 
        counter+=1
        
    for i in range(500):
        testing_set.append(raw_data[shuffled_numbers[counter]])
        counter+=1


#5 
def model():
    build_raw_data()
    split_data()
    X, Y, test_model = feature_selection()
    # text_to_vector(training_set)

    clf = MultinomialNB()
    clf.fit(X,Y)

    y_pred =  (clf.predict(test_model))
    # print(y_pred)

    print("Accuracy: ", accuracy_score(y_true, y_pred))
    print(classification_report(y_true, y_pred))
    print(confusion_matrix(y_true, y_pred))
    

if __name__ == "__main__":
    model()