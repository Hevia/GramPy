# GramPy

An easily readable context-free grammar text generator!


generate_items() function cotrbuted by https://github.com/tgsachse

Big thanks to https://github.com/Caleb-Shepard for help with the thinking this through!

Inspired by Daniel Shiffman's CFG coding challenge: https://www.youtube.com/watch?v=8Z9FRiW2Jlc

If you're new to using CFG's for text generation Daniel Shiffman's video on the subject is a great resource: https://www.youtube.com/watch?v=Rhqk9HYiB7Q

## How to use
* Our "Rules" dict is composed of a string key and is a list of lists
* The generate_items() function is used to insert our list of strings element by element. 
* The expansion() function takes an input list and compares each element to see if it is one of our Rules. If so it then randomly selects a corresponding list from that key value and replaces it.


## What to do
* Provide more detailed examples of using GramPy with more then just text 
* Provide functions to read and import grammars from JSON, and CSV values
