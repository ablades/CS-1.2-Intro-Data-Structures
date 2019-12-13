from flask import Flask, render_template, request, redirect, url_for
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
favorites.drop()

alaric_corpus = cleanup_source('static/main_character_scripts/Alaric.txt')
bonnie_corpus = cleanup_source('static/main_character_scripts/Bonnie.txt')
caroline_corpus = cleanup_source('static/main_character_scripts/Caroline.txt')
elena_corpus = cleanup_source('static/main_character_scripts/Elena.txt')
jeremy_corpus = cleanup_source('static/main_character_scripts/Jeremy.txt')
stefan_corpus = cleanup_source('static/main_character_scripts/Stefan.txt')
damon_corpus = cleanup_source('static/main_character_scripts/Damon.txt')

characters.insert_one(
    {"name": "Damon Salvatore",
    "img_path": "static/imgs/damon_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Damon.txt')
    }
    )
characters.insert_one(
    {"name": "Alaric Saltzman",
    "img_path": "static/imgs/alaric_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Alaric.txt')
    }
    )
characters.insert_one(
    {"name": "Caroline Forbes",
    "img_path": "static/imgs/caroline_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Caroline.txt')
    }
    )
characters.insert_one(
    {"name": "Bonnie Bennett",
    "img_path": "static/imgs/bonnie_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Bonnie.txt')
    }
    )
characters.insert_one(
    {"name": "Elena Gilbert",
    "img_path": "static/imgs/elena_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Elena.txt')
    }
    )
characters.insert_one(
    {"name": "Jeremy Gilbert",
    "img_path": "static/imgs/jeremy_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Jeremy.txt')
    }
    )
characters.insert_one(
    {"name": "Stefan Salvatore",
    "img_path": "static/imgs/stefan_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Stefan.txt')
    }
    )


words_list = cleanup_source('hist_test.txt')
narkov_sentence = NarkovChain(words_list)


app = Flask(__name__)




damon_narkov = NarkovChain(2, words_list=damon_corpus)
bonnie_narkov = NarkovChain(2, words_list=bonnie_corpus)
elena_narkov = NarkovChain(2, words_list=elena_corpus)
caroline_narkov = NarkovChain(2, words_list=caroline_corpus)
jeremy_narkov = NarkovChain(2, words_list=jeremy_corpus)
stefan_narkov = NarkovChain(2, words_list=stefan_corpus)
alaric_narkov = NarkovChain(2, words_list=alaric_corpus)

@app.route('/', methods=['GET', 'POST'])
def index():

    #Select a character
    if request.form.get('char') is not None:
        character_name = str(request.form.get('char'))
        character = db.characters.find_one({"name": character_name})

        return render_template('characterpage.html',character=character, sentence="")

    return render_template('tvd.html')

@app.route('/character/<name>', methods=['GET', 'POST'])
def characters_page(name):
    character = db.characters.find_one({"name": name})
    favorites = list(db.favorited.find({'name': name}))
    #user wants a sentence/favorited
    if request.method == 'POST':
        char_name = character['name']
        sentence = str(request.form.get('sentence'))
        order = int(request.form.get('order'))
        corpus = character['corpus']
        #user wants to favorite current sentence

        if request.form.get('favorite') is not None:
            favorites.insert_one({"char_name": char_name,
            "order": order,
            "sentence": sentence
            })
            return render_template('characterpage.html',character=character, sentence=sentence, favorites=favorites)
        #user wants a sentence
        else:
            #build sentence with order and corpus
            sentence = NarkovChain(order,corpus).create_sentence()
            return render_template('characterpage.html',character=character, sentence=sentence, favorites=favorites)

    return render_template('characterpage.html', character=character, sentence="", favorites=favorites)



if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))