def ask_for_input():
    while True:
        guess=input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            break 
        else:
            print ("Invalid letter. Please, enter a single alphabetical character")
    check_guess(guess)
    

def check_guess(guess):
    import random
    word_list=["lychee", "pear", "cherry", "coconut", "tomato"]
    secret_word = (random.choice(word_list))
    guess=guess.lower()
    if guess in secret_word:
        print (f"Good guess! {guess} is in the word.")
    else:
        print (f"Sorry, {guess} is not in the word Try again.")

ask_for_input()



    
