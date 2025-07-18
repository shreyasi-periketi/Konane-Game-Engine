import game_rules, random
import copy

NEG_INF = -1000000000
POS_INF = 1000000000

class Player(object):
    """ This is the player interface that is consumed by the GameManager. """
    def __init__(self, symbol): self.symbol = symbol # 'x' or 'o'

    def __str__(self): return str(type(self))

    def selectInitialX(self, board): return (0, 0)
    def selectInitialO(self, board): pass

    def getMove(self, board): pass

    def h1(self, board, symbol):
        return -len(game_rules.getLegalMoves(board, 'o' if self.symbol == 'x' else 'x'))


# This class is the code for a deterministic player.
class MinimaxPlayer(Player):
    def __init__(self, symbol, depth):
        super(MinimaxPlayer, self).__init__(symbol)
        self.depth=depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]
    def getMove(self,board):
        return self.Max_Value(board,self.depth,self.symbol)[1]


    def Max_Value(self, board, depth, symbol):
        legalMoves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legalMoves) == 0:
            return (self.h1(board, symbol), None)
        best = (NEG_INF, None)
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            if symbol == 'x':
                val = self.Min_Value(nextBoard, depth - 1, 'o')[0]
            else:
                val = self.Min_Value(nextBoard, depth - 1, 'x')[0]
            if best[0] < val:
                best = (val, legalMoves[i])
        return best

    def Min_Value(self, board, depth, symbol):
        legalMoves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legalMoves) == 0:
            return (self.h1(board, symbol), None)
        best = (POS_INF, None)
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            if symbol == 'x':
                val = self.Max_Value(nextBoard, depth - 1, 'o')[0]
            else:
                val = self.Max_Value(nextBoard, depth - 1, 'x')[0]
            if best[0] > val:
                best = (val, legalMoves[i])
        return best
    

# This class is the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth): 
        super(AlphaBetaPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        return self.AlphaBetaSearch(board)[1]
    def AlphaBetaSearch(self, board):
        return self.Max_Value(board, -1000000000, 1000000000, self.depth, self.symbol)

    def Max_Value(self, board, a, b, depth, symbol):
        # set initial max value to minus infinity
        #val = -1000000000
        # get legalmoves
        legalMoves = game_rules.getLegalMoves(board,symbol)
        best = (-1000000000, None)
        # return utility when no more legalmoves
        if (len(legalMoves) == 0 or depth == 0):
            return (self.h1(board, symbol), None)
        
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            #nextBoard = game_rules.makeMove(board, legalMoves[i])
            # when meet depth limit, then use heuristic function to replace the val Min_Value
            if symbol == 'x':
                val = self.Min_Value(nextBoard, a, b, depth - 1, 'o')[0]
            else:
                val = self.Min_Value(nextBoard, a, b, depth - 1, 'x')[0]
            if best[0] < val:
               best = (val,legalMoves[i])
            if (best[0] >= b):
                return best
            if (a < best[0]):
                a = best[0]
        return best

    def Min_Value(self, board, a, b, depth, symbol):
        # set initial max value to minus infinity
        #val = 1000000000
        # get legalmoves
        legalMoves = game_rules.getLegalMoves(board, symbol)
        best = (1000000000, None)
        # return utility when no more legalmoves
        if (len(legalMoves) == 0 or depth == 0):
            return (self.h1(board, symbol), None)
        for i in range(len(legalMoves)):
            nextBoard = game_rules.makeMove(board, legalMoves[i])
            #nextBoard = game_rules.makeMove(board, legalMoves[i])
            # when meet depth limit, then use heuristic function to replace the val Min_Value
            if symbol == 'x':
                val = self.Max_Value(nextBoard, a, b, depth - 1, 'o')[0]
            else:
                val = self.Max_Value(nextBoard, a, b, depth - 1, 'x')[0]
            if best[0] > val:
                best = (val, legalMoves[i])
            if (best[0] <= a):
                return best
            if (b > best[0]):
                b = best[0]
        return best

class RandomPlayer(Player):
    def __init__(self, symbol):
        super(RandomPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        validMoves = game_rules.getFirstMovesForX(board)
        return random.choice(list(validMoves))

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return random.choice(list(validMoves))

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return random.choice(legalMoves)
        else: return None



class DeterministicPlayer(Player):
    def __init__(self, symbol): super(DeterministicPlayer, self).__init__(symbol)

    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return legalMoves[0]
        else: return None


class HumanPlayer(Player):
    def __init__(self, symbol): super(HumanPlayer, self).__init__(symbol)
    def selectInitialX(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def selectInitialO(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def getMove(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')


def makePlayer(playerType, symbol, depth=1):
    player = playerType[0].lower()
    if player   == 'h': return HumanPlayer(symbol)
    elif player == 'r': return RandomPlayer(symbol)
    elif player == 'm': return MinimaxPlayer(symbol, depth)
    elif player == 'a': return AlphaBetaPlayer(symbol, depth)
    elif player == 'd': return DeterministicPlayer(symbol)
    else: raise NotImplementedException('Unrecognized player type {}'.format(playerType))

def callMoveFunction(player, board):
    if game_rules.isInitialMove(board): return player.selectInitialX(board) if player.symbol == 'x' else player.selectInitialO(board)
    else: return player.getMove(board)
