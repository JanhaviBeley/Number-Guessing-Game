#Janhavi Beley 
#Number Guessing Game #Introduction to Computer Science (CS112)
import random

class Player:
    def __init__(self, name, catchphrase):
        self.name = name
        self.catchphrase = catchphrase
        self.gamesWon = 0

    def __str__(self):
        return f"{self.name} - Games won: {self.gamesWon}"

    def updateGamesWon(self):
        self.gamesWon += 1

def playGuessingGame(player1, player2):
    secret_number = random.randint(1, 100)

    def get_guess(player):
        guess = int(input(f"{player.name}, guess the number between 1 and 100: "))
        return guess

    for _ in range(3):
        guess1 = get_guess(player1)
        if guess1 == secret_number:
            print(f"Congratulations, {player1.name}! That's correct.")
            player1.updateGamesWon()
            break
        elif guess1 < secret_number:
            print(f"{player1.name}, your guess is too low.")
        else:
            print(f"{player1.name}, your guess is too high.")

        guess2 = get_guess(player2)
        if guess2 == secret_number:
            print(f"Congratulations, {player2.name}! That's correct.")
            player2.updateGamesWon()
            break
        elif guess2 < secret_number:
            print(f"{player2.name}, your guess is too low.")
        else:
            print(f"{player2.name}, your guess is too high.")

    print("\nEnd of round:")
    print(player1)
    print(player2)
    print("------------------------")

if __name__ == "__main__":
    player1 = Player("Player 1", "Catchphrase 1")
    player2 = Player("Player 2", "Catchphrase 2")

    for round_number in range(1, 4):
        print(f"Round {round_number}:")
        playGuessingGame(player1, player2)

    if player1.gamesWon > player2.gamesWon:
        winner = player1
    elif player2.gamesWon > player1.gamesWon:
        winner = player2
    else:
        winner = None

    if winner:
        print(f"\n{winner.name} is the overall winner with catchphrase: {winner.catchphrase}")
    else:
        print("\nIt's a tie! No overall winner.")