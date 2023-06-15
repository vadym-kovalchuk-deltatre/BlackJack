"""Black Jack 21"""
from lib import cards
from lib.Player import Player

# region Main functions
user: Player = Player("User")
dealer: Player = Player("Dealer")
is_game_over: bool = False


def print_cards():
    '''
    Print user cards and total sum
    '''
    print(f"User cards:{user.getCards()} - {user.getSum()}\n\
Dealer cards: {dealer.getCards()} - {dealer.getSum()}")


def print_winner(winner: str) -> None:
    '''
    Print name of winner
    '''
    print(f"    {winner.upper()} WIN!")


def check_winner(total_sum: int) -> int:
    """
    The function "check_winner" takes an integer input "total_sum" and
    returns 1 if it is equal to 21, -1
    if it is greater than 21, and 0 if it is less than 21.

    :param total_sum: The total sum of points in a game, likely in a card game like Blackjack
    :type total_sum: int
    :return: The function `check_winner` takes an integer argument
    `total_sum` and returns an integer
    value based on the following conditions:
    """
    if total_sum == 21:
        return 1  # winner
    if total_sum > 21:
        return -1  # looser
    return 0  # draw


def find_closest_winner() -> None:
    """
    The function compares the sum of cards held by the dealer
    and the user in a card game and prints the
    winner or a draw.
    """
    if (dealer_sum := dealer.getSum()) > (user_sum := user.getSum()):
        print_winner("dealer")
    elif dealer_sum < user_sum:
        print_winner("User")
    else:
        print("Draw")


def get_is_game_over(winner: int) -> bool:
    """
    The function checks if the game is over by checking if there is a winner.

    :param winner: The parameter "winner" is an integer that represents
    the player who has won the game.
    The value -1 represents that the game ended in a tie, 0 represents that
    the game is still ongoing,
    and 1 represents that player 1 has won the game
    :type winner: int
    :return: The function `get_is_game_over` takes an
    integer `winner` as input and returns a boolean
    value. It returns `True` if the `winner` is either -1 or 1, indicating that the game is over.
    Otherwise, it returns `False`, indicating that the game is still ongoing.
    """
    return winner in [-1, 1]


def check_user_turn(winner: int) -> None:
    """
    Check first turn, 2 cards
    """
    if winner == -1:
        print_winner("dealer")
    elif winner == 1:
        print_winner("user")


def check_dealer_turn(winner: int, is_game_over_def: bool) -> bool:
    """
    Check first turn, 2 cards
    """
    is_over = is_game_over_def
    if winner == -1:
        print_winner("user")
    elif winner == 1:
        print_winner("dealer")
    elif winner == 0:
        find_closest_winner()
        is_over = True

    return is_over


# endregion main functions

# ! Main code block

# This code block is adding two cards to both the user's and dealer's hands. The `for _ in range(2)`
# loop is iterating twice, and on each iteration, the `getCard()` function from
# the `cards` module is
# called to get a random card. The `addCard()` method is then called on both the `user` and `dealer`
# objects to add the card to their respective hands. This is done to initialize the game with two
# cards for each player.
for _ in range(2):
    user.add_card(cards.get_card())
    dealer.add_card(cards.get_card())

print_cards()
IS_USER_WIN = user.check_first_turn()
if IS_USER_WIN:
    print_winner("user")
IS_DEALER_WIN = dealer.check_first_turn()
if IS_DEALER_WIN:
    print_winner("dealer")
is_game_over: bool = (IS_USER_WIN or IS_DEALER_WIN)

while not is_game_over:
    if input("Add another card?[y, n]: ") == "y":
        user.add_card(cards.get_card())
        check_user_turn(check_winner := check_winner(user.getSum()))
        is_game_over = get_is_game_over(check_winner)
    else:
        while dealer.get_sum() <= 17:
            dealer.add_card(cards.get_card())
        is_game_over = check_dealer_turn(check_winner := check_winner(dealer.getSum()), \
                                         get_is_game_over(check_winner))
    print_cards()
