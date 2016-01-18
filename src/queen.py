

class Queen(object):
    """Queen for moving like the chess piece queen"""
    def __init__(self):
        super(Queen, self).__init__()
        self.position = (0, 0)
 
    def set_position(self, x, y):
        """setter for position"""
        self.position = (x, y)
    def get_position(self):
        """getter for posiiton"""
        return self.position

    def valid_moves(self, board):
        """returns a list all valid moves (tuple) with respect to the current board"""
        ret_val = []
        # right
        for x in range(board.get_width()):
            if x == 0:
                continue
            if board.get_tile(self.position[0]+x, self.position[1]) != 0:
                break
            else:
                ret_val.append((self.position[0]+x, self.position[1]))
        #left
        for x in range(board.get_width()):
            if x == 0:
                continue
            if board.get_tile(self.position[0]-x, self.position[1]) != 0:
                break
            else:
                ret_val.append((self.position[0]-x, self.position[1]))
        # up
        for y in range(board.get_width()):
            if y == 0:
                continue
            if board.get_tile(self.position[0], self.position[1]+y) != 0:
                break
            else:
                ret_val.append((self.position[0], self.position[1]+y))
        #down
        for y in range(board.get_width()):
            if y == 0:
                continue
            if board.get_tile(self.position[0], self.position[1]-y) != 0:
                break
            else:
                ret_val.append((self.position[0], self.position[1]-y))

        #left down diag
        for x in range(board.get_width()):
            if x == 0:
                continue
            if board.get_tile(self.position[0]-x, self.position[1]+x) != 0:
                break
            else:
                ret_val.append((self.position[0]-x, self.position[1]+x))
        #right down diag
        for x in range(board.get_width()):
            if x == 0:
                continue
            if board.get_tile(self.position[0]+x, self.position[1]+x) != 0:
                break
            else:
                ret_val.append((self.position[0]+x, self.position[1]+x))
        #left up diag
        for x in range(board.get_width()):
            if x == 0:
                continue
            if board.get_tile(self.position[0]-x, self.position[1]-x) != 0:
                break
            else:
                ret_val.append((self.position[0]-x, self.position[1]-x))
        #righ up diag
        for x in range(board.get_width()):
            if x == 0:
                continue
            if board.get_tile(self.position[0]+x, self.position[1]-x) != 0:
                break
            else:
                ret_val.append((self.position[0]+x, self.position[1]-x))


        return ret_val


       

       


