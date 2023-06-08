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

def checkWinner()->int:
    userSum = calcCards(userCards)
    dealerSum = calcCards(dealerCards)
    if userSum == 21 or userSum > dealerSum or dealerSum > 21:
        print("User win")
        return 1
    if dealerSum == 21 or dealerSum > userSum or userSum > 21:
        print("Dealer win")
        return -1
    if dealerSum == userSum:
        print("Draw")
        return 0
    if dealerSum <= 17:
        print("Dealer must take another card")
        return -2

print(userCards, dealerCards, calcCards(userCards), calcCards(dealerCards))

nextTurn: bool = True

while nextTurn:
    answer = input("Add next card: ")
    if answer =="n":
        checkWinner()
        nextTurn = False
        continue
    addCard(userCards)
