import random
import string


def get_random_word():
  
  words = [
      "python", "variable", "function", "iterator", "notebook",
      "pipeline", "dataset", "computer", "research", "analytics"
  ]
  return random.choice(words)

def make_blanks(word):
    
    return ["_" for _ in word]

class GuessWordGame:
  def __init__(self):
    self.lives = 6
    self.used = set()
    self.word = get_random_word()
    self.blanks = make_blanks(self.word)


  def prompt_for_letter(self):
    while True:
      guess = input("Guess a letter: ").strip().lower()
      if len(guess) != 1 or guess not in string.ascii_lowercase:
        print(" → Please enter a single A-Z letter.")
        continue
      if guess in self.used:
        print(" → You already tried that letter.")
        continue
      return guess

  def reveal_letters(self):
    found_any = False
    for i, ch in enumerate(self.word):
      if ch == self.letter and self.blanks[i] == "_":
        self.blanks[i] = self.letter
        found_any = True
    return found_any

  def all_blanks_filled(self):
    return "_" not in self.blanks

  def play_game(self):

    print("\nWelcome to Word Guessing!")
    print(f"The word has {len(self.word)} letters.")
    print(" ".join(self.blanks))

    while True:
      # Ask the user to guess a letter
      guess = self.prompt_for_letter()
      self.letter = guess
      self.used.add(guess)

      # Is the guessed letter in the word?
      if self.reveal_letters():
        print("\n Well done, Nice job! You found a letter.")
        print(" ".join(self.blanks))
        # Are all self.blanks filled?
        if self.all_blanks_filled():
          print("\n Congratulation! You guessed the word!")
          print(f"Word: {self.word}")
          print("GAME OVER")
          break
      else:
        # Lose a life
        self.lives -= 1
        print(f"\nNope. You lose a life. Lives left: {self.lives}")
        print(" ".join(self.blanks))

        # Have they run out of lives?
        if self.lives <= 0:
          print("\n Out of lives & Sad story!")
          print(f"The word was: {self.word}")
          print("GAME OVER")
          break

      # (loop continues to ask for another letter)


if __name__ == "__main__":
  game = GuessWordGame()
  game.play_game()

