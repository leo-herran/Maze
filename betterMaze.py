import sys
import maze
from collections import namedtuple

#Replace top row of grid with 1s and the left column with 0s. 
#This is because we either have to remove the north or west wall. 
#on the top row, the north wall is always there because it is the boundary 
#of the maze. Same for the left column. 
def makeMazeSolvable(maze):
	mazeSize = len(maze[0]);

	for j in range(mazeSize):
		maze[0][j] = 1;

	for i in range(mazeSize):
		maze[i][0] = 0;

	return maze;

#Finds and returns all pairs of horizontally/vertically valid steps in the 
#maze represented by the given grid. 
def parseGrid(grid):
	result = [];
	rowLength = len(grid[0]);

	for i in range(rowLength):
		for j in range(rowLength):

			squareInformation = getSquareInformation(i, j, grid);

			if not squareInformation['southWall']:
				result.append(((i, j), (i+1, j)));

			if not squareInformation['eastWall']:
				result.append(((i, j), (i, j+1)));

	return result;
	
#Returns a dictionary of strings to boolean values about the current 
#square (i, j) with respect to the given maze. 
#The boolean value southWall is true if the grid square to the south of 
#(i, j) is a 
def getSquareInformation(i, j, maze):
	result = {};

	mazeSize = len(maze[0]);
	result['iSmall'] = i < mazeSize - 1;
	result['jSmall'] = j < mazeSize - 1;

	if result['iSmall']:
		result['southWall'] = not (maze[i+1][j] == 0);
	else:
		result['southWall'] = True;

	if result['jSmall']:
		result['eastWall'] = not (maze[i][j+1] == 1);
	else:
		result['eastWall'] = True;

	return result;


#Prints an ASCII representation of the given maze. 
#Here maze is in int[][] form and path is either a list of tuples from start to 
#finish or false (in which case the bare maze will be printed). 
def printMaze(givenMaze, path):
	mazeSize = len(givenMaze[0]);
	wall = ':---';
	topRow = ': v ';
	bottomRow = '';

	for i in range(mazeSize-1):
		topRow += wall;
	topRow += ':';

	for i in range(mazeSize):
		bottomRow += wall;
	bottomRow += ':';

	print(topRow);
	row = '';
	rowFloor = '';
	for i in range(mazeSize):
		
		row += '|';
		rowFloor += ':';

		for j in range(mazeSize):
			currentPosition = givenMaze[i][j];
			iBig = i > 0;
			jBig = j > 0;
			squareInfo = getSquareInformation(i, j, givenMaze);
			iSmall = squareInfo['iSmall'];
			jSmall = squareInfo['jSmall'];

			if (not jSmall) and (not iSmall):
				row += '   >'; #exit of maze
			else:
				if squareInfo['eastWall']:
					row += '   |';
				else:
					row += '    ';

			if squareInfo['southWall']:
				rowFloor += '---:';
			else:
				rowFloor += '   :';

			#if i, j in path: change two chars from end of row to letter. 
			if path and (i, j) in path:
				step = maze.getAlphabetStep(path.index((i, j)));
				rowLen = len(row);
				row = row[0: rowLen - 3] + step + row[rowLen - 2:];

		print(row);
		if iSmall: print(rowFloor);
		row = '';
		rowFloor = '';
	print(bottomRow);


def main():

	#In this implementation, a 0 in the maze representation indicates 
	#that the grid square has no north wall. A 1 indicates that it has no
	#west wall. 

	mazeSize = int(sys.argv[1]);
	while mazeSize <= 1:
		print('C\'mon, that\'s not a maze.');
		mazeSize = int(input('Enter another size: '));

	betterMaze = maze.makeMaze(mazeSize);
	betterMaze = makeMazeSolvable(betterMaze);
	printMaze(betterMaze, False);

	graph = maze.makeGraph(parseGrid(betterMaze));
	path = maze.bfs((0, 0), (mazeSize - 1, mazeSize - 1), graph);
	print '';
	print 'solution:'
	printMaze(betterMaze, path);
	

if __name__ == "__main__":
	main()

	
