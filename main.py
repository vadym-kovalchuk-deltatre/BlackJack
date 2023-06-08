import cards

userCards:list[int] = [cards.getCard()]
dealerCards:list[int] = [cards.getCard()]

def calcCards(person: list[int])->int:
    sum = 0
    for digit in person:
        sum += digit
    return sum

def addCard(person:list[int]):
    person.append(cards.getCard())
    print(f"User cards:{userCards}, DealerCards:{dealerCards}")

def checkWinner()->str:
    userSum = calcCards(userCards)
    dealerSum = calcCards(dealerCards)
    if userSum == 21:
        return "User win"
    if dealerSum == 21:
        return "Dealer win"
    if userSum > 21:
        return "User loose. More than 21"
    if dealerSum > 21:
        return "Dealer loose. More than 21"
    if userSum > dealerSum:
        return "User win"
    if dealerSum > userSum:
        return "Dealer win"
print(userCards, dealerCards, calcCards(userCards), calcCards(dealerCards))

nextTurn: bool = True

while nextTurn:
    answer = input("Add next card: ")
    if answer =="n":
        print(checkWinner())
        nextTurn = False
        continue
    addCard(userCards)
