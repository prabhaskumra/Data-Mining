# Prabhas Kumra
# CS-458
# Assignment-4

import random
import nltk
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')

from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.stem import WordNetLemmatizer 
nltk.download('wordnet')
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


raw_data =[]
training_set = [] 
testing_set = []

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
        # print(i)
        # print(raw_data[i])
    
    # print(raw_data['text'])


#2
def feature_selection():
    print("beep bop")
    

#3
def text_to_vector(list):

    texts = []
    for i in range(len(list)):
        texts.append(list[i]['text'])
    
    # texts = ["good movie", "not a good movie", "did not like", "i like it", "good one"]

    # print(texts)
    tfidf = TfidfVectorizer(min_df = 0.1, max_df = 0.8, ngram_range = (1,2))
    features = tfidf.fit_transform(texts)
    result = pd.DataFrame(features.todense(), columns = tfidf.get_feature_names())
    print(result)

    print("RR")

#4
def split_data():

    shuffled_numbers = list(range(2000))
    random.Random(4).shuffle(shuffled_numbers)
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
   feature_selection()
   text_to_vector(training_set)

    

if __name__ == "__main__":
    model()