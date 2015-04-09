#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter
import chess_defs
import tkFont

root = Tkinter.Tk()
root.wm_title("PyChess")
board = chess_defs.Board()
pieceSelected = 0
move = 0

def moveCheck(piece, startPos, endPos, pawnFirstMove):
	allowed = False

	# White Pawn
	if(piece == 1):
		change = endPos - startPos
		if(pawnFirstMove == 1):
			if(change == 10 or change == 20):
				board.setPHM(startPos)	
				allowed = True
		else:
			if(change == 10):
				allowed = True

	# Black Pawn
	elif(piece == 7):
		change = endPos - startPos
		if(pawnFirstMove == 1):
			if(change == -10 or change == -20):
				board.setPHM(startPos)	
				allowed = True
		else:
			if(change == -10):
				allowed = True

	# Knights
	elif(piece == 2 or piece == 8):
		startSquare = board.getSquare(startPos)
		endSquare = board.getSquare(endPos)
		startRank = startSquare.rank_pos
		startFile = startSquare.file_pos
		endRank = endSquare.rank_pos
		endFile = endSquare.file_pos

		rankDif = abs(startRank - endRank)
		fileDif = abs(startFile - endFile)

		if((rankDif == 1 and fileDif == 2) or (rankDif == 2 and fileDif == 1)):
			allowed = True

	# Bishops
	elif(piece == 3 or piece == 9):
		change = startPos - endPos
		if((abs(change) % 11) == 0 or (abs(change) % 9) == 0):
			pieceBetween = False
			posCheck = startPos
			LR = None
			BF = startPos - endPos
			if((abs(change) % 11) == 0):
				LR = 1
			else:
				LR = 0
			if(LR == 1):
				if(BF < 0):
					posCheck = posCheck + 11
					while(posCheck < endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck + 11
				else:
					posCheck = posCheck - 11
					while(posCheck > endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck - 11
			elif(LR == 0):
				if(BF < 0):
					posCheck = posCheck + 9
					while(posCheck < endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck + 9
				else:
					posCheck = posCheck - 9
					while(posCheck > endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck - 9						
			if(pieceBetween == False):
				allowed = True

	# Rooks
	elif(piece == 4 or piece == 10):
		change = startPos - endPos
		startSting = str(startPos)[:1]
		endString = str(endPos)[:1]
		pieceBetween = False
		removedCastle = None

		if(piece == 4 and startPos == 21):
			removedCastle = "WQC"
		elif(piece == 4 and startPos == 28):
			removedCastle = "WKC"
		elif(piece == 10 and startPos == 91):
			removedCastle = "BQC"
		elif(piece == 10 and startPos == 98):
			removedCastle = "BKC"				

		# Forward and Back
		if((abs(change) % 10) == 0):
			if(change < 0):
				posCheck = startPos + 10
				while(posCheck < endPos):
					print posCheck
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck + 10
			else:
				posCheck = startPos - 10
				while(posCheck > endPos):	
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck - 10	
			if(pieceBetween == False):
				allowed = True
				print "Removed Castle: " + removedCastle
				if(removedCastle != None):
					print "this"
					board.removeCastle(removedCastle)		

		# Side to Side
		elif(startSting == endString):
			if(change < 0):
				posCheck = startPos + 1
				while(posCheck < endPos):
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck + 1
			else:
				posCheck = startPos - 1
				while(posCheck < endPos):
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck - 1						
			if(pieceBetween == False):
				allowed = True
				print "Removed Castle: " + str(removedCastle)
				if(removedCastle != None):
					board.removeCastle(removedCastle)

	# Queens			
	elif(piece == 5 or piece == 11):
		change = startPos - endPos
		startSting = str(startPos)[:1]
		endString = str(endPos)[:1]
		pieceBetween = False

		# Forward and Back
		if((abs(change) % 10) == 0):
			if(change < 0):
				posCheck = startPos + 10
				while(posCheck < endPos):
					print posCheck
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck + 10
			else:
				posCheck = startPos - 10
				while(posCheck > endPos):	
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck - 10	
			if(pieceBetween == False):
				allowed = True		

		# Side to Side
		elif(startSting == endString):
			if(change < 0):
				posCheck = startPos + 1
				while(posCheck < endPos):
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck + 1
			else:
				posCheck = startPos - 1
				while(posCheck < endPos):
					if(board.getSquare(posCheck).piece != 0):
						pieceBetween = True
					posCheck = posCheck - 1						
			if(pieceBetween == False):
				allowed = True

		# Diagonal
		elif((abs(change) % 11) == 0 or (abs(change) % 9) == 0):
			pieceBetween = False
			posCheck = startPos
			LR = None
			BF = startPos - endPos
			if((abs(change) % 11) == 0):
				LR = 1
			else:
				LR = 0
			if(LR == 1):
				if(BF < 0):
					posCheck = posCheck + 11
					while(posCheck < endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck + 11
				else:
					posCheck = posCheck - 11
					while(posCheck > endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck - 11
			elif(LR == 0):
				if(BF < 0):
					posCheck = posCheck + 9
					while(posCheck < endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck + 9
				else:
					posCheck = posCheck - 9
					while(posCheck > endPos):
						if(board.getSquare(posCheck).piece != 0):
							pieceBetween = True
						posCheck = posCheck - 9						
			if(pieceBetween == False):
				allowed = True
		
	# Kings
	elif(piece == 6 or piece == 12):
		change = startPos - endPos
		if(change == 1 or change == -1 or change == 10 or change == -10 or change == 9 or change == -9 or change == 11 or change == -11):
			allowed = True
			if(piece == 6):
				board.removeCastle("WKC")
				board.removeCastle("WQC")	
			else:
				board.removeCastle("BKC")
				board.removeCastle("BQC")	
		elif(piece == 6 and change == -2 and board.getCastle("WKC") and board.getSquare(startPos + 1).piece == 0):
			allowed = True
			board.movePiece(28, 26)
			board.removeCastle("WKC")
			board.removeCastle("WQC")
		elif(piece == 6 and change == 2 and board.getCastle("WQC") and board.getSquare(startPos - 1).piece == 0 and board.getSquare(startPos - 3).piece == 0):
			allowed = True
			board.movePiece(21, 24)
			board.removeCastle("WKC")
			board.removeCastle("WQC")
		elif(piece == 12 and change == -2 and board.getCastle("BKC") and board.getSquare(startPos + 1).piece == 0):
			allowed = True
			board.movePiece(98, 96)
			board.removeCastle("BKC")
			board.removeCastle("BQC")
		elif(piece == 12 and change == 2 and board.getCastle("BQC") and board.getSquare(startPos - 1).piece == 0 and board.getSquare(startPos - 3).piece == 0):
			allowed = True
			board.movePiece(91, 94)
			board.removeCastle("BKC")
			board.removeCastle("BQC")	



	return allowed

def takeCheck(startPos, endPos):
	canTake = False
	startSquare = board.getSquare(startPos)
	endSquare = board.getSquare(endPos)

	if(startSquare.piece != 1 and startSquare.piece != 7):
		canTake = moveCheck(startSquare.piece, startPos, endPos, None)
	else:
		change = endSquare.position - startSquare.position
		if(change == 9 or change == 11):
			canTake = True	

	return canTake	


def squareSelect(squareNum):
	global pieceSelected
	global move

	tempSquare = board.getSquare(squareNum)
	if((tempSquare.piece == 1 and move == 0) or (tempSquare.piece == 2 and move == 0) or (tempSquare.piece == 3 and move == 0) or (tempSquare.piece == 4 and move == 0) or (tempSquare.piece == 5 and move == 0) or (tempSquare.piece == 6 and move == 0) or (tempSquare.piece == 7 and move == 1) or (tempSquare.piece == 8 and move == 1) or (tempSquare.piece == 9 and move == 1) or (tempSquare.piece == 10 and move == 1) or (tempSquare.piece == 11 and move == 1) or (tempSquare.piece == 12 and move == 1)):
		for i in range(0, 120):
			tempSquare = board.getSquare(i)
			if(tempSquare.selected == 1):
				board.setSquareSelected(i, 0)
		board.setSquareSelected(squareNum, 1)
		pieceSelected = 1
		drawBoard()
	elif(pieceSelected == 1):
		pieceToMove = 99
		for i in range(0, 120):
			temp2Square = board.getSquare(i)
			if(temp2Square.selected == 1):
				pieceToMove = i
				board.setSquareSelected(i, 0)
		if(tempSquare.piece != 0):
			if(takeCheck(pieceToMove, squareNum)):
				board.movePiece(pieceToMove, squareNum)
				move = move + 1
				move = move % 2
		else:				
			if(moveCheck(board.getSquare(pieceToMove).piece, pieceToMove, squareNum, board.getSquare(pieceToMove).pawnHasMoved)):				
				board.movePiece(pieceToMove, squareNum)
			else:
				move = move - 1	
			move = move + 1
			move = move % 2	
		pieceSelected = 0
		drawBoard()		

def drawBoard():

	for i in range(0, 120):
		square = board.getSquare(i)
		
		if(square.position != 99):
			pieceNum = square.piece

			piece = "    "
			if(pieceNum == 1):
				piece = '♙'
			elif(pieceNum == 2):
				piece = '♘'
			elif(pieceNum == 3):
				piece = '♗'
			elif(pieceNum == 4):
				piece = '♖'
			elif(pieceNum == 5):
				piece = '♕'
			elif(pieceNum == 6):
				piece = '♔'
			elif(pieceNum == 7):
				piece = '♟'
			elif(pieceNum == 8):
				piece = '♞'
			elif(pieceNum == 9):
				piece = '♝'
			elif(pieceNum == 10):
				piece = '♜'
			elif(pieceNum == 11):
				piece = '♛'
			elif(pieceNum == 12):
				piece = '♚'

			uPiece = unicode(piece, 'utf-8')


			def handleClick(event, pos = square.position):
				squareSelect(pos)	
			color = "#D6C2AD"
			if(square.color == 1):
				color = "#825E39"
			squareFont = tkFont.Font(size = 36)
			
			if(square.selected == 1):
				if(color == "#D6C2AD"):
					color = "#FFFF66"
				else:
					color = "#FF6600"	
			label = Tkinter.Label(root, text = uPiece, background = color, font = squareFont)
			label.grid(row = 8 - square.rank_pos, column = square.file_pos)
			label.bind('<Button-1>', handleClick)

drawBoard()			

root.mainloop()