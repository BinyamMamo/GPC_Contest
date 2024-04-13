"""
Check the Check
PC/UVa IDs: 110107/10196 
Popularity: B 
Success rate: average 
Level: 1 
"""

def is_king_in_check(board):
    # Define the board size
    board_size = 8
    # Define the movements for each piece relative to their positions
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Function to check if the position is on the board
    def is_on_board(x, y):
        return 0 <= x < board_size and 0 <= y < board_size
    
    # Find the kings' positions
    white_king_pos = black_king_pos = None
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 'K':
                white_king_pos = (i, j)
            elif board[i][j] == 'k':
                black_king_pos = (i, j)
    
    # Function to check for checks
    def check_for_checks(king_pos, is_white):
        x, y = king_pos
        # Check for pawns
        pawn_direction = -1 if is_white else 1
        for dx in [-1, 1]:
            if is_on_board(x + pawn_direction, y + dx):
                if (is_white and board[x + pawn_direction][y + dx] == 'p') or \
                   (not is_white and board[x + pawn_direction][y + dx] == 'P'):
                    return True
        # Check for knights
        for dx, dy in knight_moves:
            if is_on_board(x + dx, y + dy):
                if (is_white and board[x + dx][y + dy] == 'n') or \
                   (not is_white and board[x + dx][y + dy] == 'N'):
                    return True
        # Check for bishops, rooks, and queens
        for dx, dy in directions:
            dist = 1
            while is_on_board(x + dx * dist, y + dy * dist):
                piece = board[x + dx * dist][y + dy * dist]
                if piece != '.':
                    if (is_white and piece in 'qrb' and (dx == 0 or dy == 0 or abs(dx) == abs(dy))) or \
                       (not is_white and piece in 'QRB' and (dx == 0 or dy == 0 or abs(dx) == abs(dy))):
                        return True
                    break
                dist += 1
        return False
    
    # Check if either king is in check
    white_in_check = check_for_checks(white_king_pos, True) if white_king_pos else False
    black_in_check = check_for_checks(black_king_pos, False) if black_king_pos else False
    
    return white_in_check, black_in_check

# board = [
#     "rnbqkbnr",
#     "pppppppp",
#     "........",
#     "........",
#     "........",
#     "........",
#     "PPPPPPPP",
#     "RNBQKBNR"
# ]
# print(is_king_in_check(board))

if __name__ == "__main__":
    # receive input
    with open('in.in', 'r') as checkboard:
        lines = checkboard.readlines()
    output = ""
    d = 1
    lines = iter(lines)
    for line in lines:
        board = []
        while line is not None and len(line) > 1:
            board.append(list(line.strip()))
            line = next(lines, None)
        
        if is_king_in_check(board) == (False, True):
            print(f"Game #{d}: black king is in check.")
        if is_king_in_check(board) == (True, False):
            print(f"Game #{d}: white king is in check.")
        if is_king_in_check(board) == (False, False):
            print(f"Game #{d}: no king is in check.")
        d += 1
        # print(is_king_in_check(board))
