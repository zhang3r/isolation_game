"""player"""
from random import randint
from time import time

class RandomPlayer():
    """Player that chooses a move randomly."""
    def move(self, game, legal_moves, time_left):
        if not legal_moves: 
            return (-1, -1)
        return legal_moves[randint(0, len(legal_moves)-1)]
class HumanPlayer():
    """Player that chooses a move according to
    user's input."""
    def move(self, game, legal_moves, time_left):
        print('\t'.join(['[%d] %s'%(i,str(move)) for i,move in enumerate(legal_moves)] ))
        
        valid_choice = False
        while not valid_choice:
            try:
                index = int(input('Select move index:'))
                valid_choice = 0 <= index < len(legal_moves)

                if not valid_choice:
                    print('Illegal move! Try again.')
            
            except ValueError:
                print('Invalid index! Try again.')
        return legal_moves[index]

class OpenMoveEvalFn():    
    def score(self, game):
        if game.get_active_player().eval_fn == self:
            legal_moves = game.get_legal_moves()
        else:
            legal_moves = game.get_opponent_moves()
        return len(legal_moves)

class CustomEvalFn():
    def score(self, game):
        return len(game.get_legal_moves()) - len(game.get_opponent_moves())

class CustomPlayer():
    """custom ai player implementation"""
    def __init__(self, search_depth=4, eval_fn=CustomEvalFn()):
        self.eval_fn = eval_fn
        self.search_depth = search_depth
        

    def move(self, game, legal_moves, time_left):
        """move implementation"""
        reflection = False
        if game.move_count == 0:
            return (game.width//2, game.height//2)
        if game.move_count == 2 and self.is_reflect(game, game.get_active_player):
            reflection = True
        if reflection:
            opponent_move_r, opponent_move_c = game.__last_player_move__[game.__inactive_player__]
            new_move = (game.height-opponent_move_c-1, game.width-opponent_move_r-1)
            return new_move
          
        best_move = (-1, -1)
        self.time_left = time_left
        if len(legal_moves) < 8:
            for depth in range(4, 10, 2):       
                move = self.alphabeta(game, depth=depth)[0]
                if time_left() > 10:
                    best_move = move
                else:
                    break
        else:
            best_move = self.alphabeta(game, depth=self.search_depth)[0]
        return best_move        

      

    def utility(self, game):
        """checks for winner and if theres no winner evaluate the board"""
        if game.is_winner(self):
            return float("inf")

        if game.is_opponent_winner(self):
            return float("-inf")

        return self.eval_fn.score(game)

    def minimax(self, game, depth=float("inf"), maximizing_player=True):
        """minimax implementation of ai"""
        moves = game.get_legal_moves()
        
        winner = game.is_winner(game.get_active_player()) or game.is_opponent_winner(game.get_active_player())
        if depth == 0 or winner: 
            move = game.get_legal_moves()[0] if len(game.get_legal_moves()) > 0 else (-1, -1)
            return move, self.utility(game)
        
        if maximizing_player:
            best_val = float("-inf")
            for move in moves:
                val = self.minimax(game.forecast_move(move), depth-1, False)[1]
                if best_val < val:
                    best_val = val
                    best_move = move
            
        else:
            best_val = float("inf")
            for move in moves:
                val = self.minimax(game.forecast_move(move), depth-1, True)[1]
                if best_val > val:
                    best_val = val
                    best_move = move
       

        return best_move, best_val

    def alphabeta(self, game, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """alpha beta implementation of ai"""
        winner = game.is_winner(game.get_active_player()) or game.is_opponent_winner(game.get_active_player())
        if depth == 0 or winner: 
            move = game.get_legal_moves()[0] if len(game.get_legal_moves()) > 0 else (-1, -1)
            return move, self.utility(game)
        moves = game.get_legal_moves()
        best_move = moves[0]
        if maximizing_player:
            val = float("-inf")
            for move in moves:   
                if self.time_left() < 15:
                    if depth != self.search_depth:
                        move = best_move
                        return move, float("inf")
                score = self.alphabeta(game.forecast_move(move), depth-1, alpha, beta, False)[1]
                if val < score:
                    best_move = move
                    val = score
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return best_move, val
        
        else:
            val = float("inf")
            for move in moves:
                score = self.alphabeta(game.forecast_move(move), depth-1, alpha, beta, True)[1]
                if val > score:
                    best_move = move
                    val = score
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return best_move, val
        return best_move, val


    def is_reflect(self, game, player):
        opponent_move = game.__last_player_move__[game.__inactive_player__]
        unreflectable = [(0,1), (0,4),(1,0),(4,0),(5,1), (5,4),(1,5),(4,5)]
        return opponent_move not in unreflectable
