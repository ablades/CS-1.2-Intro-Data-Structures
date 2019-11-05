from flask import Flask, render_template, request, url_for

from histogram import read_file, histogram_dictonary
from sample import better_words



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    words = read_file('hist_test.txt')
    number_of_words = 10
    histogram = histogram_dictonary(words)

    #user has inputed a number for the sentence length
    if request.method == 'POST':
        number_of_words = request.form.get('word_count')

    sentence = better_words(number_of_words, len(words), histogram)
    return render_template('index.html', sentence=sentence)