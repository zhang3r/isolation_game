""" isolation Game"""
from board import Board
from queen import Queen

class Isolation(object):
    """docstring for Isolation"""
    def __init__(self):
        super(Isolation, self).__init__()

    def run(self):
        # x and y of playing field
        width = input('enter the width of the board')
        width = int(width)
        height = input('enter the height of the board')
        height = int(height)
        board = Board(width, height)
        curr_play = 0
        init_pos_player_1 = input('enter the inital position of player 1 as a tuple (x, y)')
        init_pos_player_2 = input('enter the inital position of player 2 as a tuple (x, y)')
        p1_split = init_pos_player_1.split(',')
        p2_split = init_pos_player_2.split(',')
        player_1 = Queen()
        player_1.set_position(int(p1_split[0]), int(p1_split[1]))
        board.set_tile(1, player_1.get_position()[0], player_1.get_position()[1])
        player_2 = Queen()
        player_2.set_position(int(p2_split[0]), int(p2_split[1]))
        board.set_tile(2, player_2.get_position()[0], player_2.get_position()[1])


        # inital position of player 1
        # inital pos of player 2
        players = [player_1, player_2]
        while len(players[curr_play].valid_moves(board)) != 0:
            #print board
            board.print_board()
            print('valid moves')
            avail_moves = players[curr_play].valid_moves(board)
            print(avail_moves)
            #player to pick a move
            in_pos_player = input('enter the move of player {0} as a tuple (x, y)'.format(curr_play+1))
            split = in_pos_player.split(',')

            move = (int(split[0]), int(split[1]))
            #if move is valid
            if move in avail_moves:
                #update board
                current_pos = players[curr_play].get_position()
                board.set_tile(-1, current_pos[0], current_pos[1])
                players[curr_play].set_position(move[0], move[1])
                #new position
                current_pos = players[curr_play].get_position()
                board.set_tile(curr_play+1, current_pos[0], current_pos[1])
            else:
                raise ValueError('not in move set')
               

            #update turn
            curr_play += 1
            curr_play &= 2
            
        #end of loop
        print('player {0} lost! player {1} won!'.format(players[curr_play], players[curr_play-1]))


def main():
    """main method to run isolation"""
    isolation = Isolation()
    isolation.run()

if __name__ == '__main__':
    main()
