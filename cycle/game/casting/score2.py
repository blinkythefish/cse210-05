from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor

class Score2 (Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(810, 0)
        self._velocity = Point(0, 0)
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player 2: {self._points}")
<<<<<<< HEAD
        
    
    def reset_points(self):
        '''
            resets the players points
        '''
        self._points = 0
=======
>>>>>>> f8742ae41fe9cba273431b13b1424a468f935bf7
