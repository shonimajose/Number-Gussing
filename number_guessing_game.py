import random

from colorama import init 
init(autoreset=True)

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


def number_guessing_game():
    print(f"\n{GREEN}Welcome to the Number Guessing Game!{RESET}")
    print(f"{GREEN}Choose your difficulty level{RESET}")
    print("\n1. Easy (15 attempts, range 1 to 50)")
    print("2. Medium (10 attempts, range 1 to 100)")
    print("3. Hard (5 attempts, range 1 to 200)")
    
    while True:
        choice =input("\nEnter the choice you want : ")
        if choice == "1":
            max_attempts =15
            number_range =50
            break
        elif choice == "2":
            max_attempts = 10
            number_range = 100 
            break
        elif choice =="3":
            max_attempts = 5
            number_range = 200
            break
        else :
            print(f"{RED} Invalid choice ! Please enter 1,2 or 3{RESET}") 
            
            
    
    number_guess = random.randint(1,number_range)
    attempts =0
    
    print(f"{BLUE}You have selected a number between 1 and {number_range}. Try to guess it!{RESET}")
    print(f"{BLUE}You have {max_attempts} attempts.{RESET}")    
    while attempts < max_attempts:
        remaining_attempts = max_attempts - attempts
        guess = input(f"\n{BLUE}Enter your guess (You have {remaining_attempts} attempts left): {RESET}")
        if not guess.isdigit():
           print(f"{RED}Please enter a valid number!!!!!{RESET}")
           continue   

        guess = int(guess)
        
        if guess < 1 or guess > number_range:
            print(f"{RED}ERROR !!!!!Your guess must be between 1 and {number_range}. Please try again.{RESET}")
            continue

        attempts += 1
           
        if guess < number_guess:
            print(f"{YELLOW}Too low! Try again.{RESET}")
            
        elif guess> number_guess:
            print(f"{YELLOW}Too high! Try again.{RESET}")
        else:
            print(f"{GREEN}Congratulations! You've guessed the number in {attempts} attempts.{RESET}")
            break
        if attempts == max_attempts:
            print(f"{RED}Sorry, you've run out of attempts!!!!! The correct number was {number_guess}.{RED}")
            break
        
        
    play_again = input(f"{BLUE}Do you want to play again? (y/n): {RESET}").strip().lower()
    if play_again == "y":
        number_guessing_game()
    print(f"{GREEN}Thanks for playing! Goodbye.{RESET}")

    
    
def get_input(prompt):
    return input(f"{BLUE}{prompt}{RESET}")

    
if __name__ == "__main__":
    number_guessing_game()