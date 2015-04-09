BOARD_SQUARES = 120
MAX_GAME_MOVES = 2048

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)
def enums(**enums):
    return type('Enum', (), enums)      

Piece = enum('EMPTY', 'wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK')
File = enum('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'NONE')
Rank = enum('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NONE')
Color = enum('WHITE', 'BLACK', 'BOTH')
Position = enums(A1 = 21, B1 = 22, C1 = 23, D1 = 24, E1 = 25, F1 = 26, G1 = 27, H1 = 28,
	A2 = 31, B2 = 32, C2 = 33, D2 = 34, E2 = 35, F2 = 36, G2 = 37, H2 = 38,
	A3 = 41, B3 = 42, C3 = 43, D3 = 44, E3 = 45, F3 = 46, G3 = 47, H3 = 48,
	A4 = 51, B4 = 52, C4 = 53, D4 = 54, E4 = 55, F4 = 56, G4 = 57, H4 = 58,
	A5 = 61, B5 = 62, C5 = 63, D5 = 64, E5 = 65, F5 = 66, G5 = 67, H5 = 68,
	A6 = 71, B6 = 72, C6 = 73, D6 = 74, E6 = 75, F6 = 76, G6 = 77, H6 = 78,
	A7 = 81, B7 = 82, C7 = 83, D7 = 84, E7 = 85, F7 = 86, G7 = 87, H7 = 88,
	A8 = 91, B8 = 92, C8 = 93, D8 = 94, E8 = 95, F8 = 96, G8 = 97, H8 = 98, NO_SQ = 99)

class Square:
	def __init__(self, piece, file_pos, rank_pos, position, color, phm):
		self.piece = piece
		self.file_pos = file_pos
		self.rank_pos = rank_pos
		self.position = position
		self.color = color
		self.selected = 0
		self.pawnHasMoved = phm
	

class Board:
	def __init__(self):
		self.KingSq = [Position.E1, Position.E8]
		self.side = Color.WHITE
		self.enPas = Position.NO_SQ
		self.fiftyMove = 0
		self.ply = 0
		self.hisPly = 0
		self.numPiece = [32, 8, 2, 2, 2, 1, 1, 8, 2, 2, 2, 1, 1]
		self.numBigPiece = [8, 8, 16]
		self.numMajorPiece = [3, 3, 6]
		self.numMinorPiece = [4, 4, 8]
		self.castlePerm = {"WKC": True, "WQC": True, "BKC": True, "BQC": True}
		self.squares = [None] * BOARD_SQUARES
		for i in range(0, 21):
			self.squares[i] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[21] = Square(Piece.wR, File.A, Rank.ONE, Position.A1, Color.BLACK, None)
		self.squares[22] = Square(Piece.wN, File.B, Rank.ONE, Position.B1, Color.WHITE, None)	
		self.squares[23] = Square(Piece.wB, File.C, Rank.ONE, Position.C1, Color.BLACK, None)
		self.squares[24] = Square(Piece.wQ, File.D, Rank.ONE, Position.D1, Color.WHITE, None)
		self.squares[25] = Square(Piece.wK, File.E, Rank.ONE, Position.E1, Color.BLACK, None)
		self.squares[26] = Square(Piece.wB, File.F, Rank.ONE, Position.F1, Color.WHITE, None)
		self.squares[27] = Square(Piece.wN, File.G, Rank.ONE, Position.G1, Color.BLACK, None)
		self.squares[28] = Square(Piece.wR, File.H, Rank.ONE, Position.H1, Color.WHITE, None)
		self.squares[29] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[30] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[31] = Square(Piece.wP, File.A, Rank.TWO, Position.A2, Color.WHITE, 1)
		self.squares[32] = Square(Piece.wP, File.B, Rank.TWO, Position.B2, Color.BLACK, 1)	
		self.squares[33] = Square(Piece.wP, File.C, Rank.TWO, Position.C2, Color.WHITE, 1)
		self.squares[34] = Square(Piece.wP, File.D, Rank.TWO, Position.D2, Color.BLACK, 1)
		self.squares[35] = Square(Piece.wP, File.E, Rank.TWO, Position.E2, Color.WHITE, 1)
		self.squares[36] = Square(Piece.wP, File.F, Rank.TWO, Position.F2, Color.BLACK, 1)
		self.squares[37] = Square(Piece.wP, File.G, Rank.TWO, Position.G2, Color.WHITE, 1)
		self.squares[38] = Square(Piece.wP, File.H, Rank.TWO, Position.H2, Color.BLACK, 1)
		self.squares[39] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[40] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[41] = Square(Piece.EMPTY, File.A, Rank.THREE, Position.A3, Color.BLACK, None)
		self.squares[42] = Square(Piece.EMPTY, File.B, Rank.THREE, Position.B3, Color.WHITE, None)	
		self.squares[43] = Square(Piece.EMPTY, File.C, Rank.THREE, Position.C3, Color.BLACK, None)
		self.squares[44] = Square(Piece.EMPTY, File.D, Rank.THREE, Position.D3, Color.WHITE, None)
		self.squares[45] = Square(Piece.EMPTY, File.E, Rank.THREE, Position.E3, Color.BLACK, None)
		self.squares[46] = Square(Piece.EMPTY, File.F, Rank.THREE, Position.F3, Color.WHITE, None)
		self.squares[47] = Square(Piece.EMPTY, File.G, Rank.THREE, Position.G3, Color.BLACK, None)
		self.squares[48] = Square(Piece.EMPTY, File.H, Rank.THREE, Position.H3, Color.WHITE, None)
		self.squares[49] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[50] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[51] = Square(Piece.EMPTY, File.A, Rank.FOUR, Position.A4, Color.WHITE, None)
		self.squares[52] = Square(Piece.EMPTY, File.B, Rank.FOUR, Position.B4, Color.BLACK, None)	
		self.squares[53] = Square(Piece.EMPTY, File.C, Rank.FOUR, Position.C4, Color.WHITE, None)
		self.squares[54] = Square(Piece.EMPTY, File.D, Rank.FOUR, Position.D4, Color.BLACK, None)
		self.squares[55] = Square(Piece.EMPTY, File.E, Rank.FOUR, Position.E4, Color.WHITE, None)
		self.squares[56] = Square(Piece.EMPTY, File.F, Rank.FOUR, Position.F4, Color.BLACK, None)
		self.squares[57] = Square(Piece.EMPTY, File.G, Rank.FOUR, Position.G4, Color.WHITE, None)
		self.squares[58] = Square(Piece.EMPTY, File.H, Rank.FOUR, Position.H4, Color.BLACK, None)
		self.squares[59] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[60] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[61] = Square(Piece.EMPTY, File.A, Rank.FIVE, Position.A5, Color.BLACK, None)
		self.squares[62] = Square(Piece.EMPTY, File.B, Rank.FIVE, Position.B5, Color.WHITE, None)	
		self.squares[63] = Square(Piece.EMPTY, File.C, Rank.FIVE, Position.C5, Color.BLACK, None)
		self.squares[64] = Square(Piece.EMPTY, File.D, Rank.FIVE, Position.D5, Color.WHITE, None)
		self.squares[65] = Square(Piece.EMPTY, File.E, Rank.FIVE, Position.E5, Color.BLACK, None)
		self.squares[66] = Square(Piece.EMPTY, File.F, Rank.FIVE, Position.F5, Color.WHITE, None)
		self.squares[67] = Square(Piece.EMPTY, File.G, Rank.FIVE, Position.G5, Color.BLACK, None)
		self.squares[68] = Square(Piece.EMPTY, File.H, Rank.FIVE, Position.H5, Color.WHITE, None)
		self.squares[69] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[70] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[71] = Square(Piece.EMPTY, File.A, Rank.SIX, Position.A6, Color.WHITE, None)
		self.squares[72] = Square(Piece.EMPTY, File.B, Rank.SIX, Position.B6, Color.BLACK, None)	
		self.squares[73] = Square(Piece.EMPTY, File.C, Rank.SIX, Position.C6, Color.WHITE, None)
		self.squares[74] = Square(Piece.EMPTY, File.D, Rank.SIX, Position.D6, Color.BLACK, None)
		self.squares[75] = Square(Piece.EMPTY, File.E, Rank.SIX, Position.E6, Color.WHITE, None)
		self.squares[76] = Square(Piece.EMPTY, File.F, Rank.SIX, Position.F6, Color.BLACK, None)
		self.squares[77] = Square(Piece.EMPTY, File.G, Rank.SIX, Position.G6, Color.WHITE, None)
		self.squares[78] = Square(Piece.EMPTY, File.H, Rank.SIX, Position.H6, Color.BLACK, None)
		self.squares[79] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[80] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[81] = Square(Piece.bP, File.A, Rank.SEVEN, Position.A7, Color.BLACK, 1)
		self.squares[82] = Square(Piece.bP, File.B, Rank.SEVEN, Position.B7, Color.WHITE, 1)	
		self.squares[83] = Square(Piece.bP, File.C, Rank.SEVEN, Position.C7, Color.BLACK, 1)
		self.squares[84] = Square(Piece.bP, File.D, Rank.SEVEN, Position.D7, Color.WHITE, 1)
		self.squares[85] = Square(Piece.bP, File.E, Rank.SEVEN, Position.E7, Color.BLACK, 1)
		self.squares[86] = Square(Piece.bP, File.F, Rank.SEVEN, Position.F7, Color.WHITE, 1)
		self.squares[87] = Square(Piece.bP, File.G, Rank.SEVEN, Position.G7, Color.BLACK, 1)
		self.squares[88] = Square(Piece.bP, File.H, Rank.SEVEN, Position.H7, Color.WHITE, 1)
		self.squares[89] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[90] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)
		self.squares[91] = Square(Piece.bR, File.A, Rank.EIGHT, Position.A8, Color.WHITE, None)
		self.squares[92] = Square(Piece.bN, File.B, Rank.EIGHT, Position.B8, Color.BLACK, None)	
		self.squares[93] = Square(Piece.bB, File.C, Rank.EIGHT, Position.C8, Color.WHITE, None)
		self.squares[94] = Square(Piece.bQ, File.D, Rank.EIGHT, Position.D8, Color.BLACK, None)
		self.squares[95] = Square(Piece.bK, File.E, Rank.EIGHT, Position.E8, Color.WHITE, None)
		self.squares[96] = Square(Piece.bB, File.F, Rank.EIGHT, Position.F8, Color.BLACK, None)
		self.squares[97] = Square(Piece.bN, File.G, Rank.EIGHT, Position.G8, Color.WHITE, None)
		self.squares[98] = Square(Piece.bR, File.H, Rank.EIGHT, Position.H8, Color.BLACK, None)
		for i in range(99, 120):
			self.squares[i] = Square(Piece.EMPTY, File.NONE, Rank.NONE, Position.NO_SQ, Color.BOTH, None)

	def printBoard(self):
		counter = 1
		print('_______________________')
		for i in self.pieces:
			print(' | ' + str(i.piece))
			print('__')
			if(counter == 10):
				print('\n')
				counter = 0
			counter = counter + 1

	def getSquare(self, num):
		return self.squares[num]

	def setSquareSelected(self, num, selected):
		self.squares[num].selected = selected

	def movePiece(self, startSquare, finishSquare):
		movingPiece = self.squares[startSquare].piece
		self.squares[startSquare].piece = Piece.EMPTY
		self.squares[finishSquare].piece = movingPiece

	def setPHM(self, square):
		self.squares[square].pawnHasMoved = 1

	def getCastle(self, num):
		return self.castlePerm[num]

	def removeCastle(self, num):
		self.castlePerm[num] = False								
					

