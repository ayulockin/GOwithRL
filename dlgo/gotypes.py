import enum
from collections import namedtuple

## Implementing players represented by color of the player.
## This class is also responsible for changing turns.
# Pass in the keyvalue of the player to this class
class Player(enum.Enum):
    black = 1
    white = 2
    # This function will alternate the player
    def other(self):
        if self==Player.white:
            return Player.black
        else:
            return Player.white

## Implementing coordinates on the board, will use tuple as it is imutable.
## Keep record of the current point.
## neighbours() return all the points adjacent to the current point
##class Point(namedtuple('Point', 'row col')):
##    def neighbours(self):
##        return [Point(self.row-1, self.col), Point(self.row+1, self.col),
##                Point(self.row, self.col-1), Point(self.row, self.col+1)]
##
##
##
class Point():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getPoint(self):
        return((self.row, self.col))

    def getNeighbours(self):
        return([(self.row-1, self.col), (self.row+1, self.col),
                (self.row, self.col-1), (self.row, self.col+1)])

