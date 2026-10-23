
import random

WORDS = ["apple", "tiger", "chair", "plant", "water"]
MAX_INCORRECT_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def get_guess(guessed_letters):
    while True:
        try:
            guess = input("Guess a letter: ").lower().strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Exiting the game.")
            raise SystemExit(0)

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        return guess


def play_game(secret_word=None):
    secret_word = (secret_word or choose_word()).lower()
    hidden_word = ["_"] * len(secret_word)
    guessed_letters = []
    incorrect_guesses = 0

    print("================================")
    print("      WELCOME TO HANGMAN!")
    print("================================")
    print(f"The word has {len(secret_word)} letters.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES and "_" in hidden_word:
        print("\nWord:", " ".join(hidden_word))
        print("Incorrect guesses left:", MAX_INCORRECT_GUESSES - incorrect_guesses)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    hidden_word[index] = guess
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

    print("\n================================")
    if "_" not in hidden_word:
        print("Congratulations! You won!")
        print("The word was:", secret_word)
        return True

    print("Game over! You lost.")
    print("The correct word was:", secret_word)
    return False


def main():
    print("Welcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    play_game()


if __name__ == "__main__":
    main()
