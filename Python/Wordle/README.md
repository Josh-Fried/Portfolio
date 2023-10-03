# Wordle 
### Project Overview

Challenge: Make a reproduction of Wordle that has the same user experience.

Tools: Python and PyCharm 

Team: Joshua Fried (solo project)
### How To Play 

### Rules: 

The user has 6 attempts to guess a random 5 letter word that is chosen from the word bank. Users can only guess words that are in the word bank. With every guess the letters turn green, yellow, or gray.

![#6aaa64](https://placehold.co/15x15/6aaa64/6aaa64.png) Green means that the letter is in the answer word and the letter is in that position.

![#c9b458](https://placehold.co/15x15/c9b458/c9b458.png) Yellow means the the letter is in the answer word, but not in that position.

![#787c7e](https://placehold.co/15x15/787c7e/787c7e.png) Gray means that the letter is not in the answer word.

The user tries to guess the answer word in the least attempts possible. If the user fails to guess the word in 6 attempts then they lose. My version choses a new word every time the program is launched instead of every day.
