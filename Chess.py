row7 = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]
row6 = ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]
row5 = ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"]
row4 = ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"]
row3 = ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"]
row2 = ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"]
row1 = ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]
row0 = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

grid = [row0, row1, row2, row3, row4, row5, row6, row7]

def PlaceWhitePiece():
    WhitePiece = input("Please write down the coordinates where you want to place the white piece (e.g., 'a1', 'b2'): ")
    PieceAndLocation = WhitePiece.split()
    Piece = PieceAndLocation[0]
    Location = PieceAndLocation[1]

    col = "abcdefgh".index(Location[0])  # Converting letters into 0-7
    row = int(Location[1:]) - 1          # Converting  1-8 into 0-7
    
    # Update the grid
    grid[7 - row][col] = "W"  # Place the white piece (row inverted because grid is defined from a1 upwards)
    print("White piece placed successfully.")
    print("Updated grid:")
    for row in grid:
        print(row)

PlaceWhitePiece()