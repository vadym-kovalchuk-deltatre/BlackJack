# The Player class represents a player in a card game and includes methods for adding cards, getting
# the sum of the player's cards, and checking if it is the first turn of the game.
from typing import List


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._cards = []

    def _change_ace(self) -> None:
        """
        This function changes the value of an Ace card from 11 to 1 in a list of cards.
        """
        for card in self._cards:
            if card[0] == 11:
                card[0] = 1
            break

    def add_card[C: (str, int)](self, card: C) -> None:
        """
        The function adds a card to a list of cards.

        :param card: The parameter "card" is a list containing two elements - an integer and a string.
        It is being passed as an argument to the method "addCard" which belongs to a class. The method
        appends this list to an instance variable called "_cards"
        :type card: list[int,str]
        """
        self._cards.append(card)

    def get_cards(self) -> List[list[str, int]]:
        return self._cards

    def get_sum(self) -> int:
        """
        This function calculates the sum of the values of cards in a deck.
        :return: the sum of the values of all the cards in the deck.
        """
        total_sum = 0
        for card in self._cards:
            total_sum += card[0]
        return total_sum

    def check_first_turn(self) -> bool:
        """
        This function checks if it is the first turn of a game and returns True if there is already a
        winner, otherwise it checks if there is an ace with a value of 11 and decreases it to 1 if
        necessary before returning False.
        :return: a boolean value. If the check_winner variable is equal to 1, then the function returns
        True. Otherwise, if check_winner is equal to -1, the function calls the _changeAce() method and
        returns False.
        """
        total_sum = self.get_sum()
        if total_sum == 21:
            return True
        if total_sum > 21:  # Has ace 11. Decrease to 1
            self._change_ace()
        return False

    def get_name(self) -> str:
        return self._name


# TEST SUITS


if __name__ == "__main__":
    from cards import Cards

    cards = Cards()
    player = Player("Bob")
    for _ in range(2):
        player.add_card(cards.get_card())
    print(f"Is Winner {player.get_name()}: {player.check_first_turn()}")
    print(player.get_cards())
    print(f"Total sum {player.get_name()}: {player.get_sum()}")

    player2 = Player("Biba")
    for i in range(2):
        player2.add_card([(cards.suits_cards[i]).pop(0), cards.suits[i]])
    print(player2.get_cards())
    print(f"Total sum {player2.get_name()}: {player2.get_sum()}")
    player2.check_first_turn()
    print(f"Total sum {player2.get_name()} after change ace: {player2.get_sum()}")
