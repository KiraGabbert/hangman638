word_list = ["apple", "pear", "berry", "grape", "banana"]
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed=["_"]*len(self.word)
        self.num_letters=len(set(self.word))
        self.num_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]
    def check_guess(self, guess):
        
            if guess in self.word:
                print (f"Good guess! {guess} is in the word.")
                for letter_index, letter in enumerate(self.word):
                    if guess==letter:
                        self.word_guessed[letter_index]=guess
                self.num_letters-=1
                print (f"Your guessed these letters of the word so far: {self.word_guessed}")
                print (f"You still have {self.num_lives} lives left!")
            else:
                self.num_lives-=1
                print (f"Sorry, {guess} is not in the word.")
                print (f"You now have {self.num_lives} lives left")
            

    def ask_for_input(self):
        while True:
            guess=input("Enter a single letter: ")
            guess=guess.lower()
            if len(guess)!=1 or guess.isalpha()!=True:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print ("You already tried that letter!")
            else:
                self.check_guess(guess)
            self.list_of_guesses.append(guess)
            break            

def play_game (word_list):        
        game = Hangman (word_list, num_lives=5)    
        while True:
            if game.num_lives == 0:
                print (f"You lost! No more lives. The secret word was: {game.word}. Try playing again.")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print (f"Congratulations! You won the game! You correctly guessed the word: {game.word}")
                break
            
play_game (word_list)
