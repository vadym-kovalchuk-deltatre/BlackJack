import cards
from Player import Player

# region Main functions
user = Player("User")
dealer = Player("Dealer")
is_game_over = False

def printCards():
    print(f"User cards:{user.getCards()} - {user.getSum()}\n\
Dealer cards: {dealer.getCards()} - {dealer.getSum()}")

def printWinner(winner:str):
    print(f"{winner.upper()} WIN!")

def checkWinner(sum:int) -> int:
        if sum == 21:
            return 1 # winner
        if sum > 21:
            return -1 # looser
        return 0 # draw

def getIsGameOver(check_winner:int) -> bool:
    return check_winner in [-1,1]

# endregion main functions

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
    has_another_turn = input("Add another card?[y, n]: ")
    if has_another_turn == "y":
        user.addCard(cards.getCard())
        check_winner = checkWinner(user.getSum())
        if check_winner == -1:
            printWinner("dealer")
        elif check_winner == 1:
            printWinner("user")
        is_game_over = getIsGameOver(check_winner)
    else:
        while dealer.getSum() <= 17:
            dealer.addCard(cards.getCard())
        check_winner = checkWinner(dealer.getSum())
        is_game_over = getIsGameOver(check_winner)
        if check_winner == -1:
            printWinner("user")
        elif check_winner == 1:
            printWinner("dealer")
        elif check_winner == 0:
            if dealer.getSum() > user.getSum():
                printWinner("dealer")
            elif dealer.getSum() < user.getSum():
                printWinner("User")
            else:
                print("Draw")
            is_game_over = True
    printCards()
