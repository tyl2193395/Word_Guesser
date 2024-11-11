import random

words = ['zelda', 'mario', 'pacman', 'sonic', 'minecraft']

def select_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    while True:
        word = select_word()
        guessed_letters = []
        attempts = 6

        while attempts > 0:
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                attempts -= 1
                print(f"Incorrect! You have {attempts} attempts left.")

            current_word = display_word(word, guessed_letters)
            print(current_word)

            if "_" not in current_word:
                print("You won!")
                break

        if attempts == 0:
            print(f"The word was: {word}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()