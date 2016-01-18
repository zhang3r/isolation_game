"""a board for the game isolation"""
class Board(object):
    """a board class for a board 
        0 - open
        1 - occupied
        -1 - invalid

    """
    def __init__(self, x, y):
        super(Board, self).__init__()
        self.width = x
        self.height = y
        self.grid = []
        #initial to 0
        self._build_map(0)

    def _build_map(self, init_val):
        """builds a clean playing board"""
        self.grid = [[] for j in range(self.height)]
        for j in range(self.height):
            self.grid[j] = [init_val for x in range(self.width)]


    def set_tile(self, val, X, Y):
        """invalidate a tile"""
        self.grid[X][Y] = val

    def get_tile(self, X, Y):
        """get the value of a tile"""
        #do not use negative indexes
        if X < 0 or Y < 0:
            return -1
        try:
            return self.grid[X][Y]
        except IndexError:
            return -1
        
    def get_width(self):
        """width getter"""
        return self.width
    def get_height(self):
        """width setter"""
        return self.height

    def print_board(self):
        """prints the board"""
        print("")
        for y in range(self.height):
            print("|", end='')
            for x in range(self.width):
                print(" {0} ".format(self.grid[x][y]), end='')
            print("|\n", end='')



    def __str__(self):
        """print method"""
