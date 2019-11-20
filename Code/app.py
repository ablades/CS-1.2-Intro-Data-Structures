from flask import Flask, render_template, request, url_for
from pymongo import MongoClient
from histogram import read_file, histogram_dictonary
from utils import cleanup_source
from markov import MarkovChain
from sample import better_words
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/csmarkov')

client = MongoClient(host=host)
client = MongoClient(host=f'{host}?retryWrites=false')
#Database associated with Client
db = client.get_default_database()

favorited = db.favorited

words_list = cleanup_source('hist_test.txt')
markov_sentence = MarkovChain(words_list)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    length = 10
    #user has favorited an item
        #add to db
    if request.args.get('favorite') is not None:
        favorited.insert_one(
                            {'sentence': markov_sentence.sentence,
                             'upvotes': 0,
                             'downvotes': 0
                            })
        print(f'Favorited ID {favorited.inserted_id}')
        # TODO: Add toast message saying it was inserted


    #set length to user inputed length
    if request.args.get('sentence length'):
        length = int(request.args.get('sentence length'))

    #user has upvoted a post
        #update count

    #user has downvoted a post
        #update count

    #user has inputed a number for the sentence length

    sentence = markov_sentence.create_sentence(length=length)

    favorited_list = favorited.find()
    print(favorited_list)

    return render_template('index.html', sentence=sentence, favorites=list(favorited_list))



    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))