__author__ = '50144'
from random import randint

print ("This is a Hangman simulator.")
words=["Haggis","Hello","Jamaica","Romania","Anant","Computers","Neopolitan"]

def get_word():
   global word
   random=randint(0,len(words)-1)
   word=words[random]
   word=word.lower()

def print_word(correct_or_not):
   print("\nThis is the word: ")
   x=0
   for letter in word:
       if correct_or_not[x]==1:
           print(letter,end=" ")
       else:
           print("_",end=" ")
       x+=1



def check_text(guess):
   a="Hello"
   not_allowed="!@#$%^&*()_+-=}{[]:\"';.,></?1234567890"
   a=0
   for non_allowed in not_allowed:
       if non_allowed==guess:
           a=1
   if a==1:
       print("You can only input text: ")
       make_guess()

def make_guess():
   global guess
   guess=input("\n\nGuess a letter: ")
   if len(guess)==1:
       pass
   else:
       print("You can only input a single character")
       make_guess()
   check_text(guess)

def game():
   lives=5
   win=0
   get_word()
   #print("This is the word: ", word)
   guessed=[]
   #Index to store which values have been correctly guessed.
   #00101 means the third and fifth values have been guessed.
   correct_or_not=[0 for a in range(0,len(word))]
   #Index code needed to win the game. i.e. all 1s will win#
   win_code=[1 for a in range(0,len(word))]
   while lives>0 and win==0:
       print_word(correct_or_not)
       make_guess()
       if guess in guessed:
           print("You have already guessed that. Guess again!")
           print_word(correct_or_not)
           make_guess()
       a=0
       correct_guess=0
       for letter in word:
           if letter==guess:
               print("You correctly guessed", guess)
               correct_or_not[a]=1
               correct_guess=1
           a+=1
       if correct_guess==0:
           print("Incorrect guess: ")
           lives-=1
           print("You have "+str(lives)+" lives left.")
       guessed.append(guess)
       print("These are the words already guessed", guessed)
       if correct_or_not==win_code:
           win=1
   print_word(correct_or_not)
   if win==1:
       print("\nCongratulations! You won!")
       again=input("Want to play again?(Y/N)")
       again[0].lower()
       if again=="y":
           game()

   if lives==0:
       print("\n\nYou lose sucker!!!")
       again=input("Want to play again?(Y/N)")
       again[0].lower()
       if again=="y":
           game()
game()

