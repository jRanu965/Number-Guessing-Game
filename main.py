# Import random module to generate a random number
import random 

# Function to get a valid integer input with error handling
def get_valid_integer(prompt): 
    while True: 
        try: 
            value = int(input(prompt)) 
            return value 
        except ValueError: 
            print("Invalid input. Please enter an integer.")

# Function to get a valid 'y' or 'n' response from the user
def get_yes_no(prompt): 
    while True: 
        response = input(prompt).lower() 
        if response in ['y', 'n']: 
            return response 
        else: 
            print("Invalid input. Please enter 'y' or 'n'.")


# Function to play one round of the game
def play_game():  


# Ask for number range
low_number = get_valid_integer("Enter the lowest number in the range: ")
high_number = get_valid_integer("Enter the highest number in the range: ")

# Ensure low_number is less than high_number
if low_number >= high_number:
    print("The lowest number must be less than the highest number.")
    exit()

# Ask for number of attempts
max_attempts = get_valid_integer("Enter the maximum number of attempts: ") 


# Generate random number
secret_number = random.randint(low_number, high_number) 


# Track number of attempts
attempts = 0

# Loop for user guesses

# Check if guess is too low or too high

# Display success message if guessed correctly

# If max attempts are used up, reveal the correct number

# Main game loop

# Ask for user's name and greet them

# Ask if they want to play again, only accepting 'y' or 'n'

# Run the game
