class Move():
    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = False
        self.is_resign = False

        @classmethod
        def play(cls, point):
            return Move(point=point)

        @classmethod
        def pass_turn(cls):
            return Move(is_pass=True)

        @classmethod
        def resign(cls):
            return Move(is_resign=True)



class GoString():
    def __init__(self, color, stones, liberties):
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point):
        return self.liberties.remove(point)

    def add_liberty(self, point):
        return self.liberties.add(point)

    def merge_with(self, gostring):
        assert gostring.color == self.color
        combined_stones = self.stones | gostring.stones
        combined_liberties = (self.liberties | gostring.liberties) - combined_liberties

        return GoString(self.color, combined_stones,
                        combined_liberties)

    def num_liberties(self):
        return len(self.liberties)


class Board():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        ## To keep track of board state internally.
        ## Store strings of stones in dict.
        self._grid = dict()

    def place_stone(self, player, point):
        '''
        inspect all the neighbouring stones for the given point for liberties.

        For the given point check for all the neighbouring stones and
        calculate liberties.
        '''
        adj_same_color = list()
        adj_diff_color = list()
        liberties = []




    ## Utilities

    def is_on_grid(self, point):
        
        








