print("Rock Paper Scissors Game")
#take in user input and store it in a variable
print("Enter 'r' for rock, 'p' for paper, 's' for scissors")
user_score = 0;
computer_score = 0;
rounds = 0;

while True:
    rounds += 1
    user_input = input("Enter a option: ")
    #convert the user input to lowercase
    user_input = user_input.lower()
    #warn user if user input is valid
    while user_input not in ['r', 'p', 's']:
        print("Invalid input, please try again")
        user_input = input("Enter a option: ")
        user_input = user_input.lower()

    #compare user input to the computer input
    import random
    options = ['r', 'p', 's']
    computer_input = random.choice(options)
    print(f"Computer chose {computer_input}")
    #make variables to track user score and computer score
 

    if user_input == computer_input:
        print("It's a tie")
    elif user_input == 'r' and computer_input == 's':
        print("You win")
        user_score += 1
    elif user_input == 'p' and computer_input == 'r':
        print("You win")
        user_score += 1
    elif user_input == 's' and computer_input == 'p':
        print("You win")
        user_score += 1
    else:
        print("You lose")
        computer_score += 1
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")
    print(f"Rounds: {rounds}")
    #ask user if they want to play again
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() != 'y':
        break
print("Thanks for playing")


