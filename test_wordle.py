from wordle import WordleGame, load_words

def main():
    g = WordleGame(["crane", "abbey", "slate"], answer="crane")
    print(g.over, g.won)    # False False
    g.guess("slate")
    print(g.over, g.won)    # False False
    g.guess("crane")
    print(g.over, g.won)    # True True
    print(g.attempts_left)  # 4

if __name__ == "__main__":
    main()