import random
import sys

def makeMaze(rowLength):
	grid = []
	for i in range(rowLength):
		grid.append(makeRandomRow(rowLength))
	
	for i in range(rowLength):
		print(grid[i])
	
	parseGrid(grid)

def makeRandomRow(rowLength):
	row = []
	for i in range(rowLength):
		if bool(random.getrandbits(1)):
			row.append('.')
		else: 
			row.append('0')

	return row


def parseGrid(grid):
	rowLength = len(grid[0])
	for i in range(rowLength):
		for j in range(rowLength):
			if grid[i][j] == '0':
				adjacentPositions = getPossibleConnections(i, j, rowLength)
				for position in adjacentPositions:
					if grid[position[0]][position[1]] == '0':
						print('(' + str(i) + ',' + str(j) + ')' + ' to ' + '(' + str(position[0]) + ',' + str(position[1]) + ')') 

def getPossibleConnections(i, j, rowLength):
	result = []
	iBigEnough = i-1 >= 0
	iSmallEnough = i+1 < rowLength
	jBigEnough = j-1 >= 0
	jSmallEnough = j+1 < rowLength

	if iBigEnough and jBigEnough: result.append((i-1, j-1))
	if iSmallEnough and jBigEnough: result.append((i+1, j-1))
	if iBigEnough and jSmallEnough: result.append((i-1, j+1))
	if iSmallEnough and jSmallEnough: result.append((i+1, j+1))

	return result	

mazeSize = sys.argv[1]

makeMaze(int(mazeSize))

