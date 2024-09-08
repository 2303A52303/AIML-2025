import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
current_player = "X"
board = [""] * 9

buttons = []

def check_winner():

    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    
    if "" not in board:
        return "Tie"
    
    return None

def button_click(index):
    global current_player
    
    if buttons[index]["text"] == "" and check_winner() is None:
        buttons[index]["text"] = current_player
        board[index] = current_player
        
        winner = check_winner()
        
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        else:

            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button["text"] = ""

for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 40), width=5, height=2, 
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
