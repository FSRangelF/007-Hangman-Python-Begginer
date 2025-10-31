import random
from hangman_words import word_list
import hangman_art

def display(letters, live_number):
  disp = ""
  for item in letters:
    disp += item
  # TODO-6: - Update the code below to tell the user how many lives they have left.
  print(f"****************************{lives}/6 LIVES LEFT****************************")
  print(hangman_art.stages[live_number])
  return disp

chosen_word = random.choice(word_list)
wordsize = len(chosen_word)
placeholder = []
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
lives = 6
game_over = False

for letter in chosen_word:
  placeholder.append(" _ ")

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

show = display(placeholder, lives)
print(show)

while not game_over:
  guess = input("Guess a letter: ").lower()
  count = 0

  # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in placeholder:
    print("this letter was already used")

  for i in range(0, wordsize):
    if guess == chosen_word[i]:
      placeholder[i] = guess

  if guess not in chosen_word:
    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life")

  # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
  show = display(placeholder, lives)
  print(show)

  if " _ " not in show:
    game_over = True
    print("****************************YOU WIN****************************")

  if lives == 0:
    game_over = True
    # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
    print(f"***********************YOU LOSE! The word to gues was {chosen_word.upper()} **********************")

print("Game Over!")
