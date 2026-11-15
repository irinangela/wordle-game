from collections import Counter
import random
import json

def load_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)   

def is_valid_word(word, word_set):
    return word in word_set

def unique_guess(guess, history):
    return guess not in [g for g, _ in history]

def is_win(guess, word):
    return guess == word

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

class WordleGame:
    def __init__(self, word_list, max_attempts=6, answer=None):
        if answer:
            self.answer = answer.lower()
        else:
            self.answer = random.choice(word_list).lower()
        self.valid_words = set(word_list)
        self.max_attempts = max_attempts
        self.history = []

    def guess(self, guess):
        guess = guess.strip().lower()
        if self.over:
            return "game_over"
        elif len(guess) != len(self.answer):
            return "wrong_length"
        elif not is_valid_word(guess, self.valid_words):
            return "not_a_word"
        elif not unique_guess(guess, self.history):
            return "duplicate"
        feedback = get_feedback(self.answer, guess)
        self.history.append((guess, feedback))
        return "ok"

    @property
    def won(self):
        if not self.history:
            return False
        last_guess, _ = self.history[-1]
        return is_win(last_guess, self.answer)
    
    @property
    def over(self):
        return self.won or len(self.history) >= self.max_attempts

    @property
    def attempts_left(self):
        return self.max_attempts - len(self.history)
