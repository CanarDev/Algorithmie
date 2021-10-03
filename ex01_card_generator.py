import random

def GenerateCard(First_Number):
    card = [First_Number]
    lenght = len(card)
    while sum(card) % 10 != 0 or lenght > 16:
        del card[1:]
        for i in range(0, 15):
            card.append(random.randint(0, 9))
            CardNumber = int(card[i])
            if i % 2 != 0:
                if CardNumber * 2 > 9:
                    CardNumber = CardNumber * 2 - 9
                else:
                    CardNumber = CardNumber * 2
    if sum(card) % 10 == 0:
        return print(card)



UserChoice = input("For create a new credit card, you need to choose between Mastercard and Visa")
UserChoice = UserChoice.upper()
while UserChoice != "VISA" and UserChoice != "MASTERCARD":
    UserChoice = input(f"You need to put visa or mastercard for create a new credit card")
    UserChoice = UserChoice.upper()
if UserChoice == "VISA":
    First_Number = 4
elif UserChoice == "MASTERCARD":
    First_Number = 5

GenerateCard(First_Number)