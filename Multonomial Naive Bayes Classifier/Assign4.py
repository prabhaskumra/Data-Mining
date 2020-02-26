# Prabhas Kumra
# CS-458
# Assignment-4

import nltk
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')

from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.stem import WordNetLemmatizer 
nltk.download('wordnet')
from nltk.tokenize import word_tokenize


#1
def build_raw_data():

    raw_data =[]
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
        # print(" ")
        # print(raw_data[i])


#2
def feature_selection():
    print("beep bop")
    

#3
def text_to_vector():
    print("RR")

#4
def split_data():
    print("hahaahahah")


#5 
def model():
   build_raw_data()
   feature_selection()

    

if __name__ == "__main__":
    model()