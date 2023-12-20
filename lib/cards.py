"""Main placeholder for Cards"""
import random
from typing import List, Tuple

from BlackJack.lib.suits import Suits


def get_suits() -> Tuple[str, ...]:
    """
    The get_suits function returns a tuple of strings representing the four suits in a standard deck of cards.

    :return: A tuple of all the suits in a deck
    """
    return tuple([item.value for item in Suits])


def get_random_suit_index() -> Suits:
    """
    The get_random_suit_index function returns a random suit from the deck.

    :return: A random suit from the deck
    """

    def _get_shuffled_suits() -> list[Suits]:
        """
        The _get_shuffled_suits function returns a tuple of the suits in the deck, but shuffled.

        :return: A tuple of shuffled suits
        """
        shuffled_suits = list(Suits)
        random.shuffle(shuffled_suits)

        return shuffled_suits

    return random.choice(_get_shuffled_suits())


class Cards(object):
    """The Cards class is a placeholder for a card game."""

    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the initial state of the object, and it's where you define
        the attributes that are available to all instances of this class.  In this case, we're defining a list attribute called 'cards' which will be used to store a deck of cards.

        :param self: Refer to the current instance of the class
        :return: The object itself
        """
        self.suited_cards = None
        self.refresh()

    def refresh(self) -> None:
        """The `refresh` method in the `Cards` class is used to reset
        the deck of cards. It initializes the `cards` list with the values of the cards
        (Ace to 10), and then creates a copy of this
        list for each suit in the `suits_cards` list. This ensures that each suit has its own set of
        cards.
        """
        ace = 11
        cards_list: List[int] = [ace] + list(range(2, ace))
        self.suited_cards = dict(
            zip(
                tuple(Suits),
                [cards_list.copy() for _ in range(len(cards_list))],
            )
        )

    def update_chosen_cards(func):
        """
        The update_chosen_cards function is a decorator that takes in a function and returns the same function with an additional
            action. The additional action is to remove the card from the suited_cards dictionary after it has been chosen. This
            ensures that no duplicate cards are chosen.

        :param func: Pass in the remove_card function
        :return: A function that removes a card from the list of suited_cards
        """

        def _remove_card(self):
            """
            The _remove_card function is a wrapper for the remove_card function.
            It removes a card from the deck and then removes that card from its suit in
            the suited_cards dictionary. This allows us to keep track of which cards are
            still available in each suit.

            :param self: Refer to the object itself
            :return: A tuple of the card and its suit
            """
            card = func(self)
            self.suited_cards[card[1]].remove(card[0])
            return card

        return _remove_card

    @update_chosen_cards
    def get_card(self) -> List[int | Suits]:
        """
        The function "get_card" returns a randomly selected card and
        its corresponding suit from a deck of
        cards.
        :return: A list containing a string representing a card (e.g. "Ace", "King", "Queen", etc.)
        and a string representing the suit of the card
        (e.g. "Hearts", "Diamonds", "Clubs", "Spades").
        """

        suit_index = get_random_suit_index()
        suited_cards = self.suited_cards[suit_index]
        card_index: int = random.choice(suited_cards)

        return [card_index, suit_index]


#  TESTS


if __name__ == "__main__":
    cards = Cards()
    for i in range(1, 6):
        test_card = cards.get_card()
        MESSAGE = (
            "Failed" if test_card[0] in cards.suited_cards[test_card[1]] else "Pass"
        )
        print(f"{i} - {test_card} isn't in cards - {MESSAGE}")
