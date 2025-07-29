import random

def random_number(max_num):
    return random.randint(1, max_num)

def setup_game():
    try:
        max_num_str = input("What would you like to guess between 1 to:")
        max_num = int(max_num_str)
        rand_num = random_number(max_num)
        #print(rand_num) #for testing
        return input(f"Guess a number from 1 to {max_num}:"), rand_num
    except (ValueError, TypeError):
        print("Must be a positive number")
        print("")
        return setup_game()

def guess_num(guess_in, rand_num):
    try:
        guess = int(guess_in)
        if guess == rand_num:
            print("Correct")
            return guess
        if guess < rand_num:
            print("Higher")
            return guess
        if guess > rand_num:
            print("Lower")
            return guess   
    except (ValueError, TypeError):
        print("Must be a number")
        guess_str = input("Guess again:")
        return guess_num(guess_str, rand_num)    

def main():
    setup_list = setup_game() #returns list first guess and random number
    guess_str = setup_list[0]
    rand_num = int(setup_list[1])
    num_guesses = 1

    guess = guess_num(guess_str, rand_num)

    while guess != rand_num:
        guess_str = input(f"Guess again:")
        num_guesses += 1
        guess = guess_num(guess_str, rand_num)
    
    print("")
    print("Well done!")
    print(f"You got it in {num_guesses} guesses")
    print("------------")
    play_again = input("Play agian? (Y/N)...")
    print("------------")
    if play_again.upper() == "Y":
        main()

print("")
print("Welcome to higher or lower.")
main()