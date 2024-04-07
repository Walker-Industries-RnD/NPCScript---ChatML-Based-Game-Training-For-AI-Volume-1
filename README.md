
# NPCScript - ChatML Based Game Training For AI: Volume 1

NPCScript is a simple project focused on bringing text based gaming to AI! Built for the Replicant Project, these are an open source base for you to bring gaming into your own AI!

This project focuses on bringing two games into LLMs; Tic Tac Toe and a 3D game similar to connect 4 (Currently called Dimensional Dominance)!

Learn More About ChatML [here](https://huggingface.co/docs/transformers/main/en/chat_templating#what-are-generation-prompts)!


## Features

- Easily inject game capabilities into your chatbot
- Free for commercial/private usage
- Over 2k games within each, housing turn numbers in the hundred thou range
- Includes Python Script Used To Generate Basis
- Easy to understand, text based format which can be setup for 2D/3D usage


## Demo 1: Tic Tac Toe



    {'role': 'user', 'content': 'Player X placed at (2, 0)'},
    {'role': 'assistant', 'content': 'Player O placed at (1, 1)'},
    {'role': 'user', 'content': 'Player X placed at (2, 2)'},
    {'role': 'assistant', 'content': 'Player O placed at (0, 2)'},
    {'role': 'user', 'content': 'Player X placed at (0, 0)'},
    {'role': 'assistant', 'content': 'Player O placed at (1, 0)'},
    {'role': 'user', 'content': 'Player X placed at (0, 1)'},
    {'role': 'assistant', 'content': 'Player O placed at (1, 2)'},
    {'role': 'computer', 'content': 'Player O wins!'},

## 3D Representation

### Setup Of Grid          

0  |  1  |  2         

1  |  -  |  -           

2  |  -  |  -           


### Final Setup

X  |  O  |  X 

X  |  O  |   

O  |  O  |  X 


## Demo 2: Dimensional Domination

Note: This is similar to Connect 4. However, the grid is 3D and you can have a vertical, horizontal or diagonal line. You can also combine them to make a snake! The grid size and number required to win can be changed but this was trained with an X and Y axis between 6 - 12 and a Z axis between 4 - 8. The Number needed to win is between 4 to 8


    {'role': 'computer', 'content': 'Board dimensions: 11x12x11 (XYZ)'},
    {'role': 'computer', 'content': 'Number needed to win: 7'},
    {'role': 'user', 'content': 'Player X placed at (11, 8, 1)'},
    {'role': 'assistant', 'content': 'Player O placed at (11, 12, 1)'},
    {'role': 'user', 'content': 'Player X placed at (11, 6, 1)'},
    {'role': 'assistant', 'content': 'Player O placed at (11, 5, 1)'},
    {'role': 'user', 'content': 'Player X placed at (10, 6, 2)'},
    {'role': 'assistant', 'content': 'Player O placed at (11, 9, 1)'},
    {'role': 'user', 'content': 'Player X placed at (9, 6, 3)'},
    {'role': 'assistant', 'content': 'Player O placed at (11, 4, 1)'},
    {'role': 'user', 'content': 'Player X placed at (11, 3, 1)'},
    {'role': 'assistant', 'content': 'Player O placed at (11, 2, 1)'},
    {'role': 'user', 'content': 'Player X placed at (10, 3, 2)'},
    {'role': 'assistant', 'content': 'Player O placed at (8, 6, 4)'},
    {'role': 'user', 'content': 'Player X placed at (11, 10, 1)'},
    {'role': 'assistant', 'content': 'Player O placed at (10, 12, 2)'},
    {'role': 'user', 'content': 'Player X placed at (10, 2, 2)'},
    {'role': 'assistant', 'content': 'Player O placed at (11, 7, 1)'},
    {'role': 'user', 'content': 'Player X placed at (10, 10, 2)'},
    {'role': 'assistant', 'content': 'Player O placed at (10, 4, 2)'},
    {'role': 'user', 'content': 'Player X placed at (7, 6, 5)'},
    {'role': 'assistant', 'content': 'Player O placed at (9, 2, 3)'},
    {'role': 'user', 'content': 'Player X placed at (10, 7, 2)'},
    {'role': 'assistant', 'content': 'Player O placed at (6, 6, 6)'},
    {'role': 'user', 'content': 'Player X placed at (9, 7, 3)'},
    {'role': 'assistant', 'content': 'Player O placed at (9, 3, 3)'},
    {'role': 'user', 'content': 'Player X placed at (9, 4, 3)'},
    {'role': 'assistant', 'content': 'Player O placed at (8, 3, 4)'},
    {'role': 'user', 'content': 'Player X placed at (10, 5, 2)'},
    {'role': 'assistant', 'content': 'Player O placed at (11, 11, 1)'},
    {'role': 'user', 'content': 'Player X placed at (7, 3, 5)'},
    {'role': 'assistant', 'content': 'Player O placed at (9, 12, 3)'},
    {'role': 'user', 'content': 'Player X placed at (10, 8, 2)'},
    {'role': 'computer', 'content': 'Player X wins!'}

### Explination Of Win

These all connect to create a sort of snake between different layers! 


## FAQ


#### What is included here?

I included the code used to train the AI as well as the tracking for 2k wins!

#### How do I use this with my LLM model?

If your LLM supports ChatML, you simply can add it to your corpus! I highly reccomend adding a "System"

#### How would this generally work?

You would initialize the game and on the user end create your own system to interact with it! For example, you could make a 3D game which takes the input of the user and sends it to the LLM as Player _ placed at (_, _, _)'}.

The computer should be a third system, being a program that detects whenever someone wins and in the case of DD also gives the area.

#### How does Dimensional Domination work?


No! I want to make more advanced games and have other non game datasets related to Project Replicant i'll be sharing soon enough!

#### Why make a 3D game in text isntead of Connect 4?

I originally wanted to do Connect 4 due to it's simplicity but a few online searches showed that they were suing those who made similar games to theirs.

With that in mind, I could not make a connect 4 database in the right mind while knowing developers might be in danger if they replicated the game. For that reason, DD is completely free and will NEVER have a patent on it.

#### Will this be the last of the project?

No! I want to make more advanced games and have other non game datasets related to Project Replicant i'll be sharing soon enough!

#### I found an error within the code and want to fix it!
PLEASE feel free to do so!
## How does Dimensional Domination Work?

Board Setup: The game randomly selects the dimensions of the board (rows, columns) and the depth (Z axis). For example, it might create a 6x6x6 or 8x8x8 board.

Winning Condition: The game randomly selects a number (between 4 and 8) that represents the number of consecutive pieces needed to win. This means that a player must place their pieces in a straight line (horizontal, vertical, or diagonal) of this length to win the game.

Gameplay:

Players take turns placing their pieces on the board. 
Each player places one piece per turn on an empty space in any part of the board.
The game continues until one of the following conditions is met:

One player achieves the winning condition
The board is completely filled, resulting in a tie.

Determining a Winner:

The check_win function checks the board after each move to determine if the current player has achieved the winning condition. It checks for horizontal, vertical, and diagonal sequences of pieces as well as mixtures of them all!
If a winning sequence is found for the current player, that player is declared the winner.
If no player achieves the winning condition and the board is completely filled, the game ends in a tie.
Game Output:


## License

[Apache 2](https://www.apache.org/licenses/LICENSE-2.0)

