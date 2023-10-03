import tkinter as tk
from tkinter import messagebox

def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']
    return None

def check_draw():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    return True

def on_click(row, col):
    if buttons[row][col]['text'] == "" and not game_over:
        buttons[row][col]['text'] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            global game_over
            game_over = True
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            global game_over
            game_over = True
        else:
            toggle_player()

def toggle_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    label.config(text=f"Player {current_player}'s turn")

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Initialize variables
current_player = "X"
game_over = False

# Create buttons for the Tic Tac Toe grid
buttons = [[None, None, None], [None, None, None], [None, None, None]]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(window, text="", width=10, height=3, command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Create a label to display the current player's turn
label = tk.Label(window, text=f"Player {current_player}'s turn", font=("Helvetica", 12))
label.grid(row=3, columnspan=3)

# Start the game
window.mainloop()
