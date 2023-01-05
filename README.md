# Overview

The goal of this project was to create a Rock, Paper, Scissors game using Python where a human can play against a computer player.

<p>&nbsp;</p>

# Project Instructions
* [x] Add on to the provided starter code
* [x] Create a player subclass that plays randomly
    > The starter `Player` class always plays `'rock'`. That's not a very good strategy! Create a subclass called `RandomPlayer` that chooses its move at random. When you call the `move` method on a `RandomPlayer` object, it should return one of `'rock'`, `'paper'`, or `'scissors'` at random. 
    >
    > Change the code so it plays a game between two `RandomPlayer` objects.
* [x] Keep score
    > The starter `Game` class does not keep score. It doesn't even notice which player won each round. Update the `Game` class so that it displays the outcome of each round, and keeps score for both players. You can use the provided `beats` function, which tells whether one move beats another one. 
    >
    > Make sure to handle ties — when both players make the same move!
* [x] Create a subclass for a human player
    > The game is a lot more interesting if you can actually play it, instead of just watching the computer play against itself. Create a `HumanPlayer` subclass, whose `move` method asks the human user what move to make. (Take another look back at the project demo to see what this can look like!)
    >
    > Set the program to play a game between `HumanPlayer` and `RandomPlayer`.
* [x] Create a player classes that remember
    > At the end of each game round, the `Game` class calls the `learn` method on each player object, to tell that player what the other player's move was. This means you can have computer players that change their moves depending on what has happened earlier in the game. To do this, you will need to implement `learn` methods that save information into instance variables.
    >
    > Create a `ReflectPlayer` class that remembers what move the opponent played last round, and plays that move this round. (In other words, if you play `'paper'` on the first round, a `ReflectPlayer` will play `'paper'` on the second round.)
    >
    > Create a `CyclePlayer` class that remembers what move it played last round, and cycles through the different moves. (If it played `'rock'` this round, it should play `'paper'` in the next round.)
    >
    > _(Something to think about: What should these classes do on the first move?)_
    >
    > Test each of these player classes versus `HumanPlayer`.
* [x] Validate user input
    > The human player might sometimes make typos. If they enter roxk instead of rock, the `HumanPlayer` code should let them try again. (See how this works in the demo if you type something in that isn't a valid move.)
* [x] Announce the winner
    > It's up to you how long the game should run. The starter code always plays three rounds, but that's not the only way it could work. You could choose to continue until the player types `quit`, or you could have the game run until one player is ahead by three points, or any other rule that makes sense to you.
    >
    > At the end of the game, have it print out which player won, and what the final scores are.
* [x] Check your code formatting
    > Use the `pycodestyle` tool to check the formatting of your code. Make the edits that it recommends, then re-run it to see fewer and fewer warnings. By the time you're done, it should display _no warnings or errors_ at all. 

<p>&nbsp;</p>


### The game starts by running the following command:
```
python3 adventure-game.py
```
or
```
./adventure-game.py
```

<p>&nbsp;</p>

### You must have Python 3 installed. Download it [here](https://www.python.org/downloads/).