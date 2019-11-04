from flask import Flask
from histogram import read_file, histogram_dictonary
from sample import better_words


app = Flask(__name__)

@app.route('/')
def hello_world():
    words = read_file('hist_test.txt')
    histogram = histogram_dictonary(words)
    sentence = better_words(10, len(words), histogram)
    return sentence