import random

def advanced_number_game():
    print("Welcome to the Advanced Number Guessing Game!")
    print("============================================")
    
    while True:
        level = input("Choose a difficulty level (easy, medium, hard): ").lower()
        
        if level not in ['easy', 'medium', 'hard']:
            print("Invalid difficulty level. Please choose again.")
            continue
        
        if level == 'easy':
            attempts = 10
            min_number, max_number = 1, 50
        elif level == 'medium':
            attempts = 7
            min_number, max_number = 1, 100
        else:
            attempts = 5
            min_number, max_number = 1, 200
            
        target_number = random.randint(min_number, max_number)
        score = attempts
        
        print(f"\nGuess a number between {min_number} and {max_number}. You have {attempts} attempts.\n")
        
        while attempts > 0:
            guess = int(input("Enter your guess: "))
            
            if guess == target_number:
                print(f"\nCongratulations! You guessed the correct number in {score - attempts + 1} attempt(s)!")
                break
            elif guess < target_number:
                print("Too low!")
            else:
                print("Too high!")
            
            attempts -= 1
            print(f"Attempts left: {attempts}")
            
        if attempts == 0:
            print(f"\nGame over! The correct number was {target_number}. Better luck next time!")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
            
    print("\nThank you for playing the Advanced Number Guessing Game!")
    
# Run the game
advanced_number_game()
                      