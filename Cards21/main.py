import lib.cards as cards
from lib.Player import Player

# region Main functions
user: Player = Player("User")
dealer: Player = Player("Dealer")
is_game_over: bool = False

def printCards():
    print(f"User cards:{user.getCards()} - {user.getSum()}\n\
Dealer cards: {dealer.getCards()} - {dealer.getSum()}")

def printWinner(winner:str) -> None:
    print(f"    {winner.upper()} WIN!")

def checkWinner(sum:int) -> int:
        if sum == 21:
            return 1 # winner
        if sum > 21:
            return -1 # looser
        return 0 # draw

def findClosestWinner() -> None:
    """
    The function compares the sum of cards held by the dealer and the user in a card game and prints the
    winner or a draw.
    """
    if (dealer_sum := dealer.getSum()) > (user_sum := user.getSum()):
        printWinner("dealer")
    elif dealer_sum < user_sum:
        printWinner("User")
    else:
        print("Draw")

def getIsGameOver(check_winner:int) -> bool:
    return check_winner in [-1,1]

def checkUserTurn(check_winner:int) -> None:
    if check_winner == -1:
        printWinner("dealer")
    elif check_winner == 1:
        printWinner("user")

def checkDealerTurn(check_winner:int, is_game_over_def:bool) -> bool:
    is_game_over = is_game_over_def
    if check_winner == -1:
        printWinner("user")
    elif check_winner == 1:
        printWinner("dealer")
    elif check_winner == 0:
        findClosestWinner()
        is_game_over = True

    return is_game_over

# endregion main functions

#! Main code block

# This code block is adding two cards to both the user's and dealer's hands. The `for _ in range(2)`
# loop is iterating twice, and on each iteration, the `getCard()` function from the `cards` module is
# called to get a random card. The `addCard()` method is then called on both the `user` and `dealer`
# objects to add the card to their respective hands. This is done to initialize the game with two
# cards for each player.
for _ in range(2):
    user.addCard(cards.getCard())
    dealer.addCard(cards.getCard())

printCards()
is_user_win = user.checkFirstTurn()
if is_user_win:
    printWinner("user")
is_dealer_win = dealer.checkFirstTurn()
if is_dealer_win:
    printWinner("dealer")
is_game_over = (is_user_win or is_dealer_win)

while not is_game_over:
    if input("Add another card?[y, n]: ") == "y":
        user.addCard(cards.getCard())
        checkUserTurn(check_winner:=checkWinner(user.getSum()))
        is_game_over = getIsGameOver(check_winner)
    else:
        while dealer.getSum() <= 17:
            dealer.addCard(cards.getCard())
        is_game_over = checkDealerTurn(check_winner:=checkWinner(dealer.getSum()), getIsGameOver(check_winner))
    printCards()
