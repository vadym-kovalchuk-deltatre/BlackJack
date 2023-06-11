# The Player class represents a player in a card game and includes methods for adding cards, getting
# the sum of the player's cards, and checking if it is the first turn of the game.
# region Player class definition
class Player:
    def __init__(self, name:str) -> None:
        self._name = name
        self._cards = []

    def _changeAce(self) -> None:
        """
        This function changes the value of an Ace card from 11 to 1 in a list of cards.
        """
        for card in self._cards:
            if card[0] == 11:
                card[0] = 1
            break

    def addCard(self, card:list[int,str]) -> None:
        """
        The function adds a card to a list of cards.

        :param card: The parameter "card" is a list containing two elements - an integer and a string.
        It is being passed as an argument to the method "addCard" which belongs to a class. The method
        appends this list to an instance variable called "_cards"
        :type card: list[int,str]
        """
        self._cards.append(card)

    def getCards(self) -> list[list[int, str]]:
        return self._cards

    def getSum(self) -> int:
        """
        This function calculates the sum of the values of cards in a deck.
        :return: the sum of the values of all the cards in the deck.
        """
        sum = 0
        for card in self._cards:
            sum += card[0]
        return sum

    def checkFirstTurn(self) -> bool:
        """
        This function checks if it is the first turn of a game and returns True if there is already a
        winner, otherwise it checks if there is an ace with a value of 11 and decreases it to 1 if
        necessary before returning False.
        :return: a boolean value. If the check_winner variable is equal to 1, then the function returns
        True. Otherwise, if check_winner is equal to -1, the function calls the _changeAce() method and
        returns False.
        """
        sum = self.getSum()
        if sum == 21:
            return True
        if sum > 21: # Has ace 11. Decrease to 1
            self._changeAce()
        return False
# endregion Player class definition