"""
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number!
"""


def bi_guess():
    list_number = range(0, 100)
    print("Please think of a number between 0 and 100!\nIs your secret number 50?"
          "\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
          "Enter 'c' to indicate I guessed correctly.")
    while True:
        enter = input()
        if enter == 'l':
            list_number = list_number[int(len(list_number)/2)+1:100]
            print("Is your secret number {}? ".format(list_number[int(len(list_number) / 2)]))
        elif enter == 'h':
            list_number = list_number[0:int(len(list_number)/2)]
            print("Is your secret number {}? ".format(list_number[int(len(list_number) / 2)]))
        elif enter == 'c':
            print("Game over. Your secret number was: {}".format(list_number[int(len(list_number) / 2)]))
            break
        else:
            print("Sorry, I did not understand your input."
                  "\nIs your secret number {}?".format(list_number[int(len(list_number) / 2)]))
            print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                  "Enter 'c' to indicate I guessed correctly.")

bi_guess()
