class Shogi:
    def __init__(self):
        self.board = [
            ["l", "n", "s", "g", "k", "g", "s", "n", "l"],
            [" ", "r", " ", " ", " ", " ", " ", "b", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", "B", " ", " ", " ", " ", " ", "R", " "],
            ["L", "N", "S", "G", "K", "G", "S", "N", "L"],
        ]
        self.players = ["Black", "White"]
        self.player_turn = 0

    def print_board(self):
        print("  9 8 7 6 5 4 3 2 1")
        for i in range(9):
            row = " ".join(self.board[i])
            print(i + 1, row)
        print("  a b c d e f g h i")

    def is_valid_move(self, from_pos, to_pos):
        # Check if the move is within the board limits
        if from_pos[0] < 0 or from_pos[0] > 8 or from_pos[1] < 0 or from_pos[1] > 8:
            return False
        if to_pos[0] < 0 or to_pos[0] > 8 or to_pos[1] < 0 or to_pos[1] > 8:
            return False

        # Check if the from position is occupied by the player's piece
        piece = self.board[from_pos[0]][from_pos[1]]
        if piece == " ":
            return False

        # Check if the move is valid for the specific piece
        # (Note: This implementation only checks the basic movement rules, not captures or special moves)
        if piece == "P" or piece == "p":  # Pawn
            if from_pos[1] != to_pos[1]:  # Pawns can only move straight
                return False
            if piece == "P":
                if to_pos[0] == from_pos[0] - 1:  # Pawns can move 1 square forward
                    return True
            elif piece == "p":
                if to_pos[0] == from_pos[0] + 1:  # Pawns can move 1 square forward
                    return True
            return False
        elif piece == "R" or piece == "r":  # Rook
            if from_pos[0] != to_pos[0] and from_pos[1] != to_pos[1]:  # Rooks can only move vertically or horizontally
                return False
            return True
        # Implement the movement rules for other pieces (lance, knight, silver, gold, bishop, king) in a similar manner

        return False

    def move_piece(self, from_pos, to_pos):
        piece = self.board[from_pos[0]][from_pos[1]]
        self.board[from_pos[0]][from_pos[1]] = " "
        self.board[to_pos[0]][to_pos[1]] = piece

    def play(self):
        while True:
            self.print_board()
            player = self.players[self.player_turn]
            print(player + "'s turn")

            move_from = input("Enter the piece's current position (e.g., a2): ")
            move_to = input("Enter the destination position: ")

            from_pos = self.parse_position(move_from)
            to_pos = self.parse_position(move_to)

            if not self.is_valid_move(from_pos, to_pos):
                print("Invalid move. Try again.")
                continue

            self.move_piece(from_pos, to_pos)
            self.player_turn = (self.player_turn + 1) % 2

    def parse_position(self, position):
        file_map = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8}
        file = file_map[position[0]]
        rank = int(position[1]) - 1
        return rank, file


# ゲームの実行例
game = Shogi()
game.play()
