# Tweet Generator: TVD

<!--Website Image-->

## About
Tweet Generator was an extremely fun project to work on. This project implements a basic form of Natural Language Processing utilizing Markov Chains. Markov Chains are structured similarly to a finite state machine model.


## Tweet Generation Methodology
The way the Tweet Generator works is divided into steps:

1. Initally, the program will take in a given text file and build a Markov chain using a [`Dictogram Structure`](dictogram.py) which is simply a Python's dictonary class extended to have additional functionality.

2. The chain is built by specifiying an *order*. The order indicates the amount of words in a given state. 

> For Instance take the sentence 
```text 
one fish two fish red fish blue fish
````
A second order chain would dictate that each state would be two words `one fish` `fish two` `two fish` etc..
each state contains all words that follow that exact sequence of characters. The higher the order the more consecutive words appear in a single state. Too high of an order will only generate sentences that already exisit in the sample text.

3. As the chain is built *start* and *stop* states are generated. Start states consists of the begining of sentencres and stop states consists of ending punctuation like `. ? !`.


4. Now the fun begins! This is the point where the chain is fully built and the sentence starts to generate. Markov chains use a form of stoicastic sampling which just simply means words are chosen based on probability.

<!--Continue writing out methodology -->


## Author

* Audaris 'Audi' Blades


## Getting Started

Simply [click here](www.ab-tweetgen.herokuapp.com) to go to the tweet generator's website. The server may take a minute or two to load up as it switches from a dormant to active state.

## Author

* Audaris 'Audi' Blades



## Technologies Used

* [Python](https://python.org/) - Programming Language
* [Flask](https://palletsprojects.com/p/flask/) - Lightweight web application framework
* [Jinja](https://palletsprojects.com/p/jinja/) - Template engine for python
* [Bootstrap](https://getbootstrap.com) - Front end framework
* [Heroku](https://heroku.com) - Application deployment site

## Acknowledgments

* Make School's CS 1.2 course provided the fondation for this assignment.
