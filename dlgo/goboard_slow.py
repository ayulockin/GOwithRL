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
