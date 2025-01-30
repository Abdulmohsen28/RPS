import random

choices = ['rock', 'paper', 'scissors']
results = {'win': 0, 'loss': 0, 'tie': 0}

def play():
    player = input("Enter rock, paper, or scissors: ").lower()
    if player not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return  # Exit the function if input is invalid

    computer = random.choice(choices)
    if player == computer:
        result = 'tie'
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        result = 'win'
    else:
        result = 'loss'

    results[result] += 1
    with open('game_results.txt', 'a') as f:
        f.write(f"Player: {player}, Computer: {computer}, Result: {result}\n")

    print(f"Computer chose {computer}. You {result}!")
    print(f"Stats - Wins: {results['win']}, Losses: {results['loss']}, Ties: {results['tie']}")

def read_results():
    try:
        with open('game_results.txt', 'r') as f:
            lines = f.readlines()
            print(f"Past game results: {len(lines)} games played.")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No past results found. Start playing to save results.")

while True:
    play()
    if input("Play again? (y/n): ").lower() != 'y':
        read_results()  # Show past results after game ends
        break
