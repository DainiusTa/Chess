def is_valid_piece(piece):
    if piece in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
        return piece

def is_valid_position(position):
    return len(position) == 2 and position[0] in 'abcdefgh' and position[1].isdigit() and 1 <= int(position[1]) <= 8

def is_lenght_valid(piece_info):
    if len(piece_info) != 2:
        print("Invalid format. Use 'piece position', e.g., pawn d4.")
        return False
    else:
        return True
    

def get_piece_and_position():
    while True:
        piece_input = input("Enter piece and position (e.g., knight a5): ").lower()
        piece_info = piece_input.split()

        if is_lenght_valid(piece_info)==False:
            continue

        piece, position = piece_info
        if not is_valid_piece(piece) or not is_valid_position(position):
            print("Invalid piece or position. Try again.")
        else:
            return piece, position

def get_black_pieces(white_position):
    black_pieces = []
    while True:
        if len(black_pieces) == 16:
            print("Maximum of 16 black pieces reached.")
            break 
        piece_input = input("Enter black piece and position (e.g., knight a2) or type 'done': ").lower()

        if piece_input == "done":
            if black_pieces:
                break
            else:
                print("Add at least one black piece before typing 'done'.")
                continue

        piece_info = piece_input.split()
        
        if is_lenght_valid(piece_info)==False:
            continue
        piece, position = piece_info
        if not is_valid_piece(piece) or not is_valid_position(position):
            print("Invalid piece or position. Try again.")
        elif any(p[1] == position for p in black_pieces):
            print(f"Position {position} is already occupied. Choose another.")
        elif position == white_position:
            print(f"Position {position} is already occupied by a white piece. Choose another.")
        else:
            black_pieces.append((piece, position))

    return black_pieces

def can_take(white_position, black_position, piece_type):
    Whiteletter, WhiteNumber = white_position
    Blackletter, BlackNumber = black_position
    file_diff = abs(ord(Whiteletter) - ord(Blackletter))
    rank_diff = abs(int(WhiteNumber) - int(BlackNumber))

    if piece_type == 'pawn': # Pawns capture diagonally, moving 1 square forward and 1 square sideways
        return file_diff == 1 and rank_diff == 1
    if piece_type == 'rook': # Rooks move in straight lines either horizontally or vertically
        return file_diff == 0 or rank_diff == 0
    if piece_type == 'knight': # Knights move in an "L" shape: 2 steps in one direction and 1 in the other
        return (file_diff, rank_diff) in [(2, 1), (1, 2)]
    if piece_type == 'bishop':  # Bishops move diagonally, which means the distance is the same in both directions
        return file_diff == rank_diff
    if piece_type == 'queen': # Queens combine the movement of rooks (straight lines) and bishops (diagonal)
        return file_diff == rank_diff or file_diff == 0 or rank_diff == 0
    if piece_type == 'king': # Kings move one square in any direction (horizontally, vertically, or diagonally)
        return file_diff <= 1 and rank_diff <= 1

    return False

def main():
    white_piece, white_position = get_piece_and_position()
    black_pieces = get_black_pieces(white_position)

    capturable = []
    for black_piece, black_position in black_pieces:
        if can_take(white_position, black_position, white_piece):
            capturable.append(f"{black_piece} at {black_position}")

    if capturable:
        print("Capturable black pieces:")
        print("\n".join(capturable))
    else:
        print("No black pieces can be captured.")

if __name__ == "__main__":
    main()