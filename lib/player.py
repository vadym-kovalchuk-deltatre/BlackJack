"""
The Player class represents a player in a card game
and includes methods for adding cards, getting
the sum of the player's cards, and checking if it is the first turn of the game.
from typing import Any, List
"""
from typing import Any


class Player:
    """The Player class is a blueprint for creating player objects."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._cards = []

    def _change_ace(self) -> None:
        """
        This function changes the value of an Ace card from 11 to 1 in a list of cards.
        """

        for _card in self._cards:
            if _card[0] == 11:
                _card[0] = 1
                print(f"Ace {_card[1]} as 11 points was changed to 1, {self.cards}")
            break

    def add_card(self, _card: list[Any]) -> None:
        """
        The function adds a card to a list of cards.

        :param card: The parameter "card" is a list containing two elements - an integer
        and a string.
        It is being passed as an argument to the method "addCard" which belongs to a class.
        The method appends this list to an instance variable called "_cards"
        :type card: list[int,str]
        @param _card:
        @type _card: list(int, Suite)
        """
        self._cards.append(_card)

    @property
    def cards(self) -> str:
        """
        The cards function returns a list of cards.

        :param self: Refer to the object itself
        :return: str of cards
        """
        pair_cards = list(map(lambda pair: str(pair[0]) + str(pair[1]), self._cards))
        return ", ".join(pair_cards)

    def get_sum(self) -> int:
        """
        This function calculates the sum of the values of cards in a deck.
        :return: the sum of the values of all the cards in the deck.
        """

        return sum([_card[0] for _card in self._cards])

    def check_first_turn(self) -> bool:
        """
        This function checks if it is the first turn of a game and returns True if there
        is already a winner, otherwise it checks if there is an ace with a value of 11
        and decreases it to 1 if necessary before returning False.
        :return: a boolean value. If the check_winner variable is equal to 1, then
        the function returns True.
        Otherwise, if check_winner is equal to -1, the function calls the _changeAce() method and
        returns False.
        """
        total_sum = self.get_sum()
        if total_sum == 21:
            return True
        if total_sum > 21:  # Has ace 11. Decrease to 1
            self._change_ace()
        return False

    @property
    def name(self) -> str:
        """
        The get_name function returns the name of the person.

        :param self: Refer to the object itself
        :return: The name of the object
        """
        return self._name

    def __str__(self) -> str:
        return str(f"{self._name}, Score: {self.get_sum()}")

    def refresh(self) -> None:
        """
        The refresh function is used to reset the deck of cards.
        It does this by setting the list of cards to an empty list.

        :param self: Represent the instance of the class
        :return: None
        """
        self._cards = []


# TEST SUITS


if __name__ == "__main__":
    from cards import Cards, Suits

    cards = Cards()
    player = Player("Bob")
    for _ in range(2):
        player.add_card(cards.get_card())
    print(f"Is Winner {player.name}: {player.check_first_turn()}")
    print(f"{player}")
    player.refresh()
    assert not player.cards
    print(f"{player} hasn't any cards and refreshed")

    player2 = Player("Baba")
    for i in range(2):
        player2.add_card(cards.get_card())
    print(f"{player2} => {player2.cards}")
    print(f"Total sum {player2.name}: {player2.get_sum()}")
    player2.check_first_turn()
    print(f"Check first turn: {player2}")

    player3 = Player("Buba")
    cards.refresh()  # refresh all cards
    for suite in [Suits.HEART, Suits.DIAMOND]:
        card = [cards.suited_cards[suite].pop(0), suite]
        player3.add_card(card)
    check_first_sum_message = "Failed" if player3.get_sum() != 22 else "Pass"
    print(
        f"For {player3} check sum is {check_first_sum_message} cards are {player3.cards}"
    )
    player3.check_first_turn()
    assert player3.get_sum() != 22
