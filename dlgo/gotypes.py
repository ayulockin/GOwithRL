import enum

## Implementing players represented by color of the player.
## This class is also responsible for changing turns.
class Player(enum.Enum):
    black = 1
    white = 2

    def other(self):
        if self==Player.white:
            return Player.black
        else:
            return Player.white

## Implementing coordinates on the board, will use tuple as it is imutable.
