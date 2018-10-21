# GramPy

An easily readable context-free grammar text generator!


generate_items() function cotrbuted by https://github.com/tgsachse

Big thanks to https://github.com/Caleb-Shepard for help with the thinking this through!

Inspired by Daniel Shiffman's CFG coding challenge: https://www.youtube.com/watch?v=8Z9FRiW2Jlc

If you're new to using CFG's for text generation Daniel Shiffman's video on the subject is a great resource: https://www.youtube.com/watch?v=Rhqk9HYiB7Q

## How to use
* Our "Rules" dict is composed of a string key and is a list of lists
* The generate_items() function is used to insert our list of strings element by element. 
* The expansion() function takes an input list and compares each element to see if it is one of our Rule's keys. If so it then randomly selects a corresponding list from that key value and replaces it in the list. After the initial for loop we perform another check to make sure our list has expanded correctly and if so we call it recursively until our list contains no more non-terminal values


## What to do
* Provide more detailed examples of using GramPy with more then just text 
* Provide functions to read and import grammars from JSON, and CSV values
* Correct the output so it outputs as a string not a list
