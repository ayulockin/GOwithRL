import copy
from dlgo.gotypes import Player

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

    ## Utilities

    def is_on_grid(self, point):
        '''
        To check if the given point is on board
        '''
        if point.row<=self.num_rows and point.col<=self.num_cols:
            return 1

    def get_color(self, point):
        '''
        To return color of the string
        '''
        string = self._grid.get(point)
        if string is None:
            return None
        return string.color

    def get_go_string(self, point):
        '''
        To return string itself
        '''
        string = self._grid.get(point)
        if string is None:
            return None
        return string


    def place_stone(self, player, point):
        '''
        inspect all the neighbouring stones for the given point for liberties.

        For the given point check for all the neighbouring stones and
        calculate liberties.
        '''
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        adj_same_color = list()
        adj_diff_color = list()
        liberties = []
    
        '''
        Check all the neighbours and calculate liberties
        '''

        for neighbour in point.getNeighbours():
            if not self.is_on_grid(neighbour):
                continue
            neighbour_string = self.get_go_string(neighbour)
            liberties.append(neighbour)
            if neighbour_string.color == player:
                if neighbour_string not in adj_same_color:
                    adj_same_color.append(neighbour_string)
            elif:
                if neighbour_string not in adj_diff_color:
                    adj_diff_color.append(neighbour_string)

        new_string = GoString(color, [point], liberties)

        ## merge any adjacent string of color
        for same_color_str in adj_same_color:
            new_str = new_str.merge_with(new_str)
        for new_str_point in new_str.stones:
            self._grid[new_str_point] = new_str
        ## reduce liberties of other color string 
        for other_color_str in adj_diff_color:
            other_color_str.remove_liberty(point)
        ## color for which liberties=0 remove them
        for other_color_str in adj_diff_color:
            if self.num_liberties(other_color_string) == 0:
                self._remove_string(other_color_str)


    def _remove_string(self, string):
        for point in string.stones:
            for neighbour in point.neighbours():
                neighbour_string =self._grid.get(neighbour)
                if neighbout_string is None:
                    continue
                if neighbour_string is not string:
                    neighbout_sting.add_liberty(point)
            self._grid[point] = None

        
class GameState():
    def __init__(self, board, next_player, previous, move):
        self.board = board
        self.next_player = next_player
        self.previous_stone = previous
        self.last_move = move


    def apply_move(self, move):
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.next_player, move.point)
        else:
            next_board = self.board
        return GameState(next_board, self.next_player.other, self, move)
        
        @classmethod
        def new_game(cls, board_size):
            if isinstance(board_size, int):
                board_size = (board_size, board_size)
                board = Board(*board_size)
            return GameState(board, Player.black, None, None)


        def is_over(self):
                if self.last_move is None:
                    return False
                if self.last_move.is_resign:
                    return True
                second_last_move = self.previous_state.last_move
                if second_last_move is None:
                    return False
                return self.last_move.is_pass and second_last_move.is_pass

        def is_move_self_capture(self, player, move):
            if not move.is_play:
                return False
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(player, move.point)
            new_string = next_board.get_go_string(move.point)
            return new_string.num_liberties == 0



        @property
        def situation(self):
            return (self.next_player, self.board)

        def does_move_violate_ko(self, player, move):
            if not move.is_play:
                return False
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(player, move.point)
            next_situation = (player.other, next_board)
            past_state = self.previous_state
            while past_state is not None:
                if past_state.situation == next_situation:
                    return True
                past_state = past_state.previous_state
            return False

        def is_valid_move(self, move):
            if self.is_over():
                return False
            if move.is_pass or move.is_resign:
                return True
            return (
                self.board.get(move.point) is None and
                not self.is_move_self_capture(self.next_player, move) and
                not self.does_move_violate_ko(self.next_player, move))

            

                







