import sys
import maze

def makeMazeSolvable(maze):
	mazeSize = len(maze[0]);

	for j in range(mazeSize):
		maze[0][j] = 1;

	for i in range(mazeSize):
		maze[i][0] = 0;

	return maze;

#Prints an ASCII representation of the given maze. 
#Here maze is in int[][] form and path is either a list of tuples from start to 
#finish or false (in which case the bare maze will be printed). 
def printMaze(maze, path):
	mazeSize = len(maze[0]);
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
			currentPosition = maze[i][j];
			iBig = i > 0;
			jBig = j > 0;
			jSmall = j < mazeSize - 1;
			iSmall = i < mazeSize - 1;

			if iSmall:
				southWall = not (maze[i+1][j] == 0)
			else:
				southWall = True;
			if jSmall:
				eastWall = not (maze[i][j+1] == 1)
			else:
				eastWall = True;

			if (not jSmall) and (not iSmall):
				row += '   >'; #exit of maze
			else:
				if eastWall:
					row += '   |';
				else:
					row += '    ';

			if southWall:
				rowFloor += '---:';
			else:
				rowFloor += '   :';

			#if i, j in path: change two chars from end of row to letter. 
			if path and (i, j) in path:
				step = getAlphabetStep(path.index((i, j)));
				rowLen = len(row);
				row = row[0: rowLen - 3] + step + row[rowLen - 2:];

		print(row);
		if iSmall: print(rowFloor);
		row = '';
		rowFloor = '';
	print(bottomRow);


def main():
	mazeSize = int(sys.argv[1]);
	while mazeSize <= 1:
		print('C\'mon, that\'s not a maze.');
		mazeSize = int(input('Enter another size: '));

	#0 = north, 1 = west. 
	theMaze = maze.makeMaze(mazeSize);
	print(theMaze);
	theMaze = makeMazeSolvable(theMaze);
	print(theMaze);
	printMaze(theMaze, False);
	

if __name__ == "__main__":
	main()

	
