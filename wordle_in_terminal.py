import random
import json
from collections import Counter

def get_feedback(word, guess):
    feedback = ['⬜'] * len(guess)
    letter_counter = Counter(word)
    for i in range(len(guess)):
        if guess[i] == word[i]:
            feedback[i] = '🟩'  # Correct letter and position
            letter_counter[guess[i]] -= 1
    for i in range(len(guess)):
        if feedback[i] == '🟩':
            continue
        if letter_counter[guess[i]] > 0:
            feedback[i] = '🟨'  # Correct letter but wrong position
            letter_counter[guess[i]] -= 1
        else:
            feedback[i] = '⬜'  # Incorrect letter
    return feedback

def is_valid_word(word, word_set):
    return word in word_set

def unique_guess(guess, history):
    return guess not in [g for g, _ in history]

def is_win(guess, word):
    return guess == word

def main():
    with open('words_english.json', 'r') as file:
        word_list = json.load(file)
        word = random.choice(word_list).lower()
        word_set = set(word_list)
    attempts = 6
    history = []
    won = False
    output = ["⬜"] * len(word)
    print('Welcome to the Word Guessing Game!\n')
    print(''.join(output))
    while attempts > 0:
        guess = input(f'Guess a {len(word)}-letter word: ').lower()
        if len(guess) != len(word):
            print(f'Please enter a {len(word)}-letter word.')
            continue
        elif not is_valid_word(guess, word_set):
            print('Invalid word. Please try again.')
            continue
        elif not unique_guess(guess, history):
            print('You have already guessed that word. Please try again.')
            continue
        output = get_feedback(word, guess)
        if is_win(guess, word):
            print('Feedback: ' + ''.join(output))
            print('Congratulations! You guessed the word correctly.')
            won = True
            break
        attempts -= 1
        history.append((guess, output))
        print('Feedback: ' + ''.join(output))
        print('\nHistory:')
        for g, f in history:
            print(f'  {g}: {"".join(f)}')
    if not won:
        print(f'Sorry, you ran out of attempts. The correct word was: {word}')

if __name__ == '__main__':
    main()