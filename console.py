from wordle import WordleGame, load_words

def main():
    game = WordleGame(load_words('words_english.json'))
    while not game.over:
        result = game.guess(input("Enter your guess: "))
        if result == "ok":
            print("Guess accepted!\n")
            for g, f in game.history:
                print(f'  {g}: {"".join(f)}')
            print (f'Attempts left: {game.attempts_left}\n')
        elif result == "wrong_length":
            print(f"Please enter a {len(game.answer)}-letter word.")
        elif result == "not_a_word":
            print("Invalid word. Please try again.")
        elif result == "duplicate":
            print("You have already guessed that word. Please try again.")
    if game.won:
        print("Congratulations! You guessed the word correctly.")
    else:
        print(f"Game over! The correct word was: {game.answer}")

if __name__ == "__main__":
    main()