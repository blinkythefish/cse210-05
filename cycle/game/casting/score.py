from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
<<<<<<< HEAD
        self.set_text(f"Score: {self._points}")
        
    def reset_points(self):
        '''
            resets the players points
        '''
        self._points = 0
=======
        self.set_text(f"Player 1: {self._points}")
>>>>>>> f8742ae41fe9cba273431b13b1424a468f935bf7
