from enum import Enum


class Suits(Enum):
    """Placeholder of card's suits"""

    HEART = "♥"
    DIAMOND = "♦"
    SPADE = "♠"
    CLUB = "♣"

    def __str__(self):
        """
        The __str__ function is called when you call str() on an object.
        It should return a string representation of the object, and that's what will be printed out.
        The __repr__ function is usually used for debugging, and it should also return a string representation of the object.

        :param self: Refer to the current instance of the class
        :return: The value of the card
        """
        return self.value
