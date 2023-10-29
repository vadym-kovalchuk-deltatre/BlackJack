"""Black Jack 21"""
from lib import utils
from lib.cards import Cards
from lib.player import Player
from lib.storedb import StoreResults

cards = Cards()
user = Player("User")
dealer = Player("Dealer")
is_game_over = False
next_game = True


def print_cards():
    """
    Print user cards and total sum
    """
    for player in (user, dealer):
        print(f"{player.name:^10}: {player.cards} = {player.get_sum()}")
    # print(f"Dealer cards: {dealer.cards} - {dealer.get_sum()}")


def print_winner(winner: Player) -> None:
    """
    The print_winner function prints the winner of a game.

    :param winner: str: Tell the function what to print
    :return: None
    """
    msg = f"{winner.name.upper()} WIN!"
    print(msg)
    utils.print_underline(len(msg))
    StoreResults().last_winner = str(winner)


def check_sum(total_sum: int) -> int:
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
    if (dealer_sum := dealer.get_sum()) > (user_sum := user.get_sum()):
        print_winner(dealer)
    elif dealer_sum < user_sum:
        print_winner(user)
    else:
        print("Draw")
        StoreResults().clean_last_winner()


def check_is_game_over(winner: int) -> bool:
    """
    The function checks if the game is over by checking if there is a winner.

    :param winner: The parameter "winner" is an integer that represents
    the player who has won the game.
    The value -1 represents that the game ended in a tie, 0 represents that
    the game is still ongoing,
    and 1 represents that player 1 has won the game
    :type winner: int
    :return: The function `check_is_game_over` takes an
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
        print_winner(dealer)
    elif winner == 1:
        print_winner(user)


def check_dealer_turn(winner: int, is_game_over_def: bool) -> bool:
    """
    Check first turn, 2 cards
    """
    is_over = is_game_over_def
    if winner == -1:
        print_winner(user)
    elif winner == 1:
        print_winner(dealer)
    elif winner == 0:
        find_closest_winner()
        is_over = True

    return is_over


def refresh_table():
    """
    The function refresh_table refreshes the cards, user,
    and dealer objects and then prints an empty line.
    """
    cards.refresh()
    user.refresh()
    dealer.refresh()
    print("")


# ! Main code block

# This code block is adding two cards to both the user's and dealer's hands. The `for _ in range(2)`
# loop is iterating twice, and on each iteration, the `getCard()` function from
# the `cards` module is
# called to get a random card. The `addCard()` method is then called on both the `user` and `dealer`
# objects to add the card to their respective hands. This is done to initialize the game with two
# cards for each player.
while next_game:
    if last_winner := StoreResults().last_winner:
        print(last_winner)
        utils.print_underline(len(last_winner) + 1)
    for _ in range(2):
        user.add_card(cards.get_card())
        dealer.add_card(cards.get_card())

    print_cards()
    IS_USER_WIN = user.check_first_turn()
    if IS_USER_WIN:
        print_winner(user)
    IS_DEALER_WIN = dealer.check_first_turn()
    if IS_DEALER_WIN:
        print_winner(dealer)
    is_game_over = IS_USER_WIN or IS_DEALER_WIN

    while not is_game_over:
        if input("Add another card?[y, n]: ").lower() == "y":
            user.add_card(cards.get_card())
            check_user_turn(check_winner := check_sum(user.get_sum()))
            is_game_over = check_is_game_over(check_winner)
            print_cards()
        else:
            while dealer.get_sum() <= 17:
                dealer.add_card(cards.get_card())
            is_game_over = check_dealer_turn(
                check_winner := check_sum(dealer.get_sum()),
                check_is_game_over(check_winner),
            )
            if is_game_over:
                print_cards()
    if input("Next turn?[y, n]: ").lower() == "y":
        refresh_table()
    else:
        next_game = False
        print("Bye!")
