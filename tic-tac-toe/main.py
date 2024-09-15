from tkinter import *
import board as b

# ** Global **
BROWN = "#4b2c34"
BEIGE = "#ddddbb"
GREEN = "#9bdeac"
BLUE = "#447878"
FONT_NAME = "Courier"
turn = 0
game_over = False

# ** Game State Setup **
game = b.Board()

# ** Game Display Setup **
window = Tk()
window.title("Tic-Tac-Toe")
window.config(padx=100, pady=100, bg=BROWN, highlightthickness=0)


# ** Two Player Game **

def two_players():

    # clear window
    welcome_label.grid_forget()
    two_button.grid_forget()


    turn_label = Label(text="Player 1's turn (X)", font=(FONT_NAME, 18, "bold"), pady=20, bg=BROWN, fg=BEIGE)
    turn_label.grid(column=1, row=0)

    win_label = Label(text="", font=(FONT_NAME, 18, "bold"), pady=20, bg=BROWN, fg=BEIGE)
    win_label.grid(column=1, row=2)

    board_canvas = Canvas(window, width=450, height=450, bg=BEIGE, highlightthickness=0)
    board_img = PhotoImage(file="board.png")
    board_canvas.create_image(225, 225, image=board_img)
    o_img = PhotoImage(file="o.png")
    x_img = PhotoImage(file="x.png")

    board_canvas.grid(column=1, row=1)

    # ** Restart Mechanics **

    def restart():
        restart_button.grid_forget()
        win_label.config(text="")
        turn_label.config(text="Player 1's turn (X)")
        board_canvas.delete("all")
        board_canvas.create_image(225, 225, image=board_img)
        game.reset()
        global turn
        turn = 0
        global game_over
        game_over = False

    restart_button = Button(text="Restart", font=(FONT_NAME, 18, "bold"), padx=30, pady=10, bg=BEIGE, fg=BROWN,
                            command=restart)

    # ** Click to Place **

    def convert_click_location(c):
        c = int(c / 75)
        if c < 2:
            c = 75
        elif c < 4:
            c = 225
        else:
            c = 375
        return c

    def clicked(event):
        x, y = event.x, event.y
        x = convert_click_location(x)
        y = convert_click_location(y)
        global game_over
        if not game_over and game.char_at(int(x / (75 * 2)), int(y / (75 * 2))) == " ":
            global turn
            if turn % 2 == 0:
                char = "x"
                turn_label.config(text="Player 2's turn (O)")
                board_canvas.create_image(x, y, anchor=CENTER, image=x_img)
            else:
                char = "o"
                turn_label.config(text="Player 1's turn (X)")
                board_canvas.create_image(x, y, anchor=CENTER, image=o_img)

            game.update(int(x / (75 * 2)), int(y / (75 * 2)), char)
            game.print_board()
            if game.check_board(char) == "Win":
                game_over = True
                print(f"{char} wins")
                turn_label.config(text="")
                if char == "x":
                    win_label.config(text="Player 1 (X) wins!")
                else:
                    win_label.config(text="Player 2 (O) wins!")
                restart_button.grid(column=1, row=3)
            elif game.check_board(char) == "Draw":
                game_over = True
                turn_label.config(text="")
                print("it's a draw")
                win_label.config(text="It's a draw!")
                restart_button.grid(column=1, row=3)
            print("click")
            turn += 1

    board_canvas.bind("<Button-1>", clicked)

# Initial Game Player Menu **

welcome_label = Label(text="Welcome to Tic-Tac-Toe", font=(FONT_NAME, 18, "bold"), pady=20, bg=BROWN, fg=BEIGE)
welcome_label.grid(column = 0, row = 0)

two_button = Button(text="Two Players", font=(FONT_NAME, 18, "bold"), padx=30, pady=10, bg=BEIGE, fg=BROWN, command=two_players)
two_button.grid(column = 0, row = 1)


window.mainloop()

