from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from histogram import read_file, histogram_dictonary
from utils import cleanup_source
from narkov import NarkovChain
from sample import better_words
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/csmarkov')

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/narkov')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

favorites = db.favorited
characters = db.characters

alaric_corpus = cleanup_source('static/main_character_scripts/Alaric.txt')
bonnie_corpus = cleanup_source('static/main_character_scripts/Bonnie.txt')
caroline_corpus = cleanup_source('static/main_character_scripts/Caroline.txt')
elena_corpus = cleanup_source('static/main_character_scripts/Elena.txt')
jeremy_corpus = cleanup_source('static/main_character_scripts/Jeremy.txt')
stefan_corpus = cleanup_source('static/main_character_scripts/Stefan.txt')
damon_corpus = cleanup_source('static/main_character_scripts/Damon.txt')

#Damon
key = {"name": "Damon Salvatore"}
value = {"name": "Damon Salvatore",
    "img_path": "imgs/damon_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Damon.txt')
    }
characters.update(key, value, upsert=True)

#Alaric
key = {"name": "Alaric Saltzman"}
value = {"name": "Alaric Saltzman",
    "img_path": "imgs/alaric_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Alaric.txt')
    }
characters.update(key, value, upsert=True)

#Caroline
key = {"name": "Caroline Forbes"}
value = {"name": "Caroline Forbes",
    "img_path": "imgs/caroline_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Caroline.txt')
    }
characters.update(key, value, upsert=True)

#Bonnie
key = {"name": "Bonnie Bennett"}
value = {"name": "Bonnie Bennett",
    "img_path": "imgs/bonnie_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Bonnie.txt')
    }
characters.update(key, value, upsert=True)

#Elena
key = {"name": "Elena Gilbert"}
value = {"name": "Elena Gilbert",
    "img_path": "imgs/elena_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Elena.txt')
    }
characters.update(key, value, upsert=True)

#Jeremy
key = {"name": "Jeremy Gilbert"}
value = {"name": "Jeremy Gilbert",
    "img_path": "imgs/jeremy_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Jeremy.txt')
    }
characters.update(key, value, upsert=True)

#Stefan
key = {"name": "Stefan Salvatore"}
value = {"name": "Stefan Salvatore",
    "img_path": "imgs/stefan_still.jpg",
    "corpus": cleanup_source('static/main_character_scripts/Stefan.txt')
    }
characters.update(key, value, upsert=True)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    #Select a character
    if request.form.get('char') is not None:
        character_name = str(request.form.get('char'))
        #character = db.characters.find_one({"name": character_name})
        return redirect(url_for('characters_page' ,name=character_name))

    return render_template('tvd.html')

@app.route('/character/<name>', methods=['GET', 'POST'])
def characters_page(name):
    character = dict(db.characters.find_one({"name": name}))
    favorites = list(db.favorited.find({'char_name': name}))
    #user wants a sentence/favorited
    if request.method == 'POST':
        char_name = character['name']
        sentence = str(request.form.get('sentence'))
        #order = int(request.form.get('order'))
        corpus = character['corpus']
        #user wants to favorite current sentence

        if request.form.get('favorite') is not None:
            db.favorited.insert_one({"char_name": char_name,
            #"order": order,
            "sentence": sentence
            })
            favorites = list(db.favorited.find({'char_name': name}))
            return render_template('characterpage.html',character=character, sentence=sentence, favorites=favorites)
        #user wants a sentence
        else:
            #build sentence with order and corpus
            sentence = NarkovChain(2,corpus).create_sentence()
            favorites = list(db.favorited.find({'char_name': name}))
            return render_template('characterpage.html',character=character, sentence=sentence, favorites=favorites)

    favorites = list(db.favorited.find({'char_name': name}))
    character = db.characters.find_one({"name": name})
    return render_template('characterpage.html', character=character, sentence="", favorites=favorites)



if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))