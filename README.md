# Isolation Game

this game is used by many AI classes for teaching purposes

##Game Rules
The rules of Isolation are simple. Two players take turns placing their
own game piece on different squares of a 5 by 5 grid. After the first two
moves (in which each player puts their piece on an unoccupied square),
the pieces move like queens in chess: diagonally, horizontally and
vertically up to the edge of the board. Each time a player moves their
piece, the square that they were previously occupying is blocked and
cannot be moved to or moved through, for the remainder of the game. In
addition, the players may not move through one another or occupy the
same square. The first player who is unable to move loses.


##Playing the Game
To play the game, navigate to where isolation.py is and run that file ' python isolation.py'

in single number inputs, enter number without spaces '1'

in tuple like inputs, enter without parentheses '1,1'

##Testing
To run tests run ' python -m unittest ' in the main directory

####Todos
Currently does not handel un even boards and bad inputs
