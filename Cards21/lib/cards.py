"""Main placeholder for Cards"""
import random
from typing import List, Tuple, Any


class Cards:
    """The Cards class is a placeholder for a card game."""

    def __init__(self):
        self.cards = []
        self.suits_cards = []
        self.suits: Tuple[str, str, str, str] = ("♥", "♦", "♠", "♣")
        self.refresh()

    def refresh(self) -> None:
        """The `refresh` method in the `Cards` class is used to reset
        the deck of cards. It initializes the `cards` list with the values of the cards
        (Ace to 10), and then creates a copy of this
        list for each suit in the `suits_cards` list. This ensures that each suit has its own set of
        cards.
        """
        self.cards: List[int] = [11] + list(range(2, 11))
        self.suits_cards = [
            self.cards.copy(),  # Hearts
            self.cards.copy(),  # Diamonds
            self.cards.copy(),  # Spades
            self.cards.copy(),  # Clubs
        ]

    def get_card(self) -> List[Any]:
        """
        The function "get_card" returns a randomly selected card and
        its corresponding suit from a deck of
        cards.
        :return: A list containing a string representing a card (e.g. "Ace", "King", "Queen", etc.)
        and a string representing the suit of the card
        (e.g. "Hearts", "Diamonds", "Clubs", "Spades").
        """

        suit_index = random.randrange(len(self._get_shuffled_suits()))
        suit_cards = self.suits_cards[suit_index]
        card_index = random.randint(0, len(suit_cards) - 1)
        card = suit_cards.pop(card_index)

        return [card, self.suits[suit_index]]

    def _get_shuffled_suits(self) -> Tuple[str,]:
        """
        The _get_shuffled_suits function returns a tuple of the suits in the deck, but shuffled.

        :param self: Pass the instance of the class to a method
        :return: A tuple of shuffled suits
        """
        shuffled_suits = list(self.suits)
        random.shuffle(shuffled_suits)

        return tuple(
            shuffled_suits,
        )  # type: ignore


#  TESTS


if __name__ == "__main__":
    cards = Cards()
    for i in range(1, 6):
        test_card = cards.get_card()
        print(test_card)
        test_suit_index = cards.suits.index(test_card[1])
        print(cards.suits_cards[test_suit_index])
        MESSAGE = (
            "Failed" if test_card[0] in cards.suits_cards[test_suit_index] else "Pass"
        )
        print(f"{i} - {MESSAGE}")
