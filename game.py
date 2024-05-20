import random
from tkinter import *
from tkinter import messagebox

# Game logic functions
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    # Update the result labels
    label_user_choice.config(text=f"Your choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}")
    label_result.config(text=f"Result: {result}")
    
    # Update scores
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    label_user_score.config(text=f"Your score: {user_score}")
    label_computer_score.config(text=f"Computer's score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_choice.config(text="Your choice:")
    label_computer_choice.config(text="Computer's choice:")
    label_result.config(text="Result:")
    label_user_score.config(text=f"Your score: {user_score}")
    label_computer_score.config(text=f"Computer's score: {computer_score}")

# Initialize the main window
root = Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place widgets
label_instruction = Label(root, text="Choose rock, paper, or scissors:")
label_instruction.pack(pady=10)

frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

button_rock = Button(frame_buttons, text="Rock", command=lambda: play_game("rock"))
button_rock.grid(row=0, column=0, padx=10)

button_paper = Button(frame_buttons, text="Paper", command=lambda: play_game("paper"))
button_paper.grid(row=0, column=1, padx=10)

button_scissors = Button(frame_buttons, text="Scissors", command=lambda: play_game("scissors"))
button_scissors.grid(row=0, column=2, padx=10)

label_user_choice = Label(root, text="Your choice:")
label_user_choice.pack(pady=5)

label_computer_choice = Label(root, text="Computer's choice:")
label_computer_choice.pack(pady=5)

label_result = Label(root, text="Result:")
label_result.pack(pady=5)

label_user_score = Label(root, text=f"Your score: {user_score}")
label_user_score.pack(pady=5)

label_computer_score = Label(root, text=f"Computer's score: {computer_score}")
label_computer_score.pack(pady=5)

button_reset = Button(root, text="Reset Game", command=reset_game)
button_reset.pack(pady=10)

# Start the main event loop
root.mainloop()