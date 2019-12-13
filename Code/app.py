from flask import Flask, render_template, request, url_for
from pymongo import MongoClient
from histogram import read_file, histogram_dictonary
from utils import cleanup_source
from narkov import NarkovChain
from sample import better_words
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/csmarkov')

client = MongoClient(host=host)
client = MongoClient(host=f'{host}?retryWrites=false')
#Database associated with Client
db = client.get_default_database()

favorites = db.favorited
characters = db.characters
characters.drop()

characters.insert_one(
    {"name": "Damon Salvatore",
    "img_path": "static/imgs/damon_still.jpg",
    }
    )
characters.insert_one(
    {"name": "Alaric Saltzman",
    "img_path": "static/imgs/alaric_still.jpg"
    }
    )
characters.insert_one(
    {"name": "Caroline Forbes",
    "img_path": "static/imgs/caroline_still.jpg"
    }
    )
characters.insert_one(
    {"name": "Bonnie Bennett",
    "img_path": "static/imgs/bonnie_still.jpg"
    }
    )
characters.insert_one(
    {"name": "Elena Gilbert",
    "img_path": "static/imgs/elena_still.jpg"
    }
    )
characters.insert_one(
    {"name": "Jeremy Gilbert",
    "img_path": "static/imgs/jeremy_still.jpg"
    }
    )
characters.insert_one(
    {"name": "Stefan Salvatore",
    "img_path": "static/imgs/stefan_still.jpg"
    }
    )

favorites.insert_one(
    {"char_name": "Damon Salvatore",
    "order": int(2),
    "sentence": "sentence",
    }
    )


words_list = cleanup_source('hist_test.txt')
narkov_sentence = NarkovChain(words_list)


app = Flask(__name__)


alaric_corpus = cleanup_source('static/main_character_scripts/Alaric.txt')
bonnie_corpus = cleanup_source('static/main_character_scripts/Bonnie.txt')
caroline_corpus = cleanup_source('static/main_character_scripts/Caroline.txt')
elena_corpus = cleanup_source('static/main_character_scripts/Elena.txt')
jeremy_corpus = cleanup_source('static/main_character_scripts/Jeremy.txt')
stefan_corpus = cleanup_source('static/main_character_scripts/Stefan.txt')
damon_corpus = cleanup_source('static/main_character_scripts/Damon.txt')

damon_narkov = NarkovChain(2, words_list=damon_corpus)
bonnie_narkov = NarkovChain(2, words_list=bonnie_corpus)
elena_narkov = NarkovChain(2, words_list=elena_corpus)
caroline_narkov = NarkovChain(2, words_list=caroline_corpus)
jeremy_narkov = NarkovChain(2, words_list=jeremy_corpus)
stefan_narkov = NarkovChain(2, words_list=stefan_corpus)
alaric_narkov = NarkovChain(2, words_list=alaric_corpus)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.form.get('char') is not None:
        character_name = str(request.form.get('char'))
        character = db.characters.find_one({"name": character_name})

        return render_template('characterpage.html', character=character)

    #user wants a setence/favorited
    if request.method == 'POST':
        #user wants to favorite current sentence
        if request.form.get('favorite') is not None:
            char_name = str(request.form.get('name'))
            sentence = str(request.form.get('sentence'))
            order = int(request.form.get('order'))
            character = db.characters.find_one({"name": char_name})
            favorites.insert_one({"char_name": "Damon Salvatore",
            "order": order,
            "sentence": sentence
            })
        #user wants a sentence
        else:
            return render_template('characterpage.html', character=character, )

        
    #length = 10
    #user has favorited an item
        #add to db
    # if request.args.get('favorite') is not None:
    #     favorited.insert_one(
    #                         {'sentence': markov_sentence.sentence,
    #                          'upvotes': 0,
    #                          'downvotes': 0
    #                         })
    #     print(f'Favorited ID {favorited.inserted_id}')


    # #set length to user inputed length
    # if request.args.get('sentence length'):
    #     length = int(request.args.get('sentence length'))

    # #user has upvoted a post
    #     #update count

    # #user has downvoted a post
    #     #update count

    # #user has inputed a number for the sentence length

    # sentence = markov_sentence.create_sentence(length=length)

    # favorited_list = favorited.find()
    # print(favorited_list)

    return render_template('tvd.html')#, sentence=sentence, favorites=list(favorited_list))



if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))