import tkinter as tk

class Board:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]

        self.buttons = [[None for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text="", font=("Helvetica", 32),
                                   width=2, height=1,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.status_label = tk.Label(master, text="Player X's turn", font=("Helvetica", 16))
        self.status_label.grid(row=3, columnspan=3)

    def handle_click(self, i, j):
        if self.board[i][j] != "":
            return
        self.board[i][j] = self.current_player
        self.buttons[i][j].configure(text=self.current_player)
        if self.check_winner():
            self.status_label.configure(text=f"Player {self.current_player} wins!")
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].configure(state="disabled")
        elif self.check_draw():
            self.status_label.configure(text="Draw!")
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.configure(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    game = Board(root)
    root.mainloop()
