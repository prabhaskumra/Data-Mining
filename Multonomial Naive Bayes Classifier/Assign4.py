# Prabhas Kumra
# CS-458
# Assignment-4

import nltk
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')

from sklearn.naive_bayes import MultinomialNB


#1
def build_raw_data():

    raw_data =[]
    for category in movie_reviews.categories():
        print(category)
        for fileid in movie_reviews.fileids(category):
            review_words = movie_reviews.words(fileid)
            review_text = ' '
            for word in review_words:
                review_text += ' ' + word
            review_dictionary = {'text':review_text, 'sentiment': category}
            raw_data.append(review_dictionary)

    print (len(raw_data))
    print (raw_data[0].text)

#2
def feature_selection():
    print(" beep bop")

#3
def text_to_vector():
    print("beep baap")

#4
def split_data():
    print("hahaahahah")


#5 
def model():
   build_raw_data()

    

if __name__ == "__main__":
    model()