import random
import sys

#Creates a random maze of size rowLength by rowLength. 
def makeMaze(rowLength):
	grid = [];
	for i in range(rowLength):
		grid.append(makeRandomRow(rowLength));
	
	return grid;

#Creates a random row of length rowLength. 
def makeRandomRow(rowLength):
	row = [];
	for i in range(rowLength):
		if bool(random.getrandbits(1)):
			row.append('.');
		else: 
			row.append('0');

	return row;


#Finds and returns all pairs of horizontally/vertically adjacent 0s 
#in the given grid. 
def parseGrid(grid):
	result = []; 
	rowLength = len(grid[0]);
	for i in range(rowLength):
		for j in range(rowLength):
			if grid[i][j] == '0':
				adjacentPositions = getPossibleConnections(i, j, rowLength);
				for position in adjacentPositions:
					x = position[0];
					y = position[1];
					if grid[x][y] == '0':
						if not ((x, y), (i, j)) in result:	
							result.append(((i, j), (x, y)));

	return result;

#For a given pair of indeces (i, j), returns some or all of the positions 
#in the grid to the left, right, up, and down, depending on the size of i and 
#j relative to rowLength.  
def getPossibleConnections(i, j, rowLength):
	result = [];
	iBigEnough = i-1 >= 0;
	iSmallEnough = i+1 < rowLength;
	jBigEnough = j-1 >= 0;
	jSmallEnough = j+1 < rowLength;

	#diagonals:
	# if iBigEnough and jBigEnough: result.append((i-1, j-1))
	# if iSmallEnough and jBigEnough: result.append((i+1, j-1))
	# if iBigEnough and jSmallEnough: result.append((i-1, j+1))
	# if iSmallEnough and jSmallEnough: result.append((i+1, j+1))

	if iBigEnough: result.append((i-1, j));
	if iSmallEnough: result.append((i+1, j));
	if jBigEnough: result.append((i, j-1));
	if jSmallEnough: result.append((i, j+1));

	return result;

#Constructs an adjacency list graph given pairs of tuples representing positions
#in a grid. 
def makeGraph(pairs):
	graph = {};
	for pair in pairs:
		pairOne = pair[0];
		pairTwo = pair[1];

		if(pairTwo == None): print('what');

		if not pairOne in graph:
			graph[pairOne] = [pairTwo];
		else :
			graph[pairOne].append(pairTwo);

		if not pairTwo in graph:
			graph[pairTwo] = [pairOne];
		else :
			graph[pairTwo].append(pairOne);

	return graph;

#Performs a breadth-first search to find the shortest path from the given 
#starting position to the given end position in the given adjacency-list graph. 
def bfs(start, end, graph):
	queue = [(start, [start])];

	while queue:
		(node, path) = queue.pop();
		
		if node in graph:
			for nextNode in graph[node]:
				if not nextNode in set(path):
					if nextNode == end:
						return path + [nextNode];
					else:
						queue.insert(0, (nextNode, path + [nextNode]));

	return False


#Prints an ASCII representation of the given maze. 
#Here maze is in char[][] form and path is either a list of tuples from start to 
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
			jSmall = j < mazeSize - 1;
			iSmall = i < mazeSize - 1;

			if (not jSmall) and (not iSmall):
				row += '   >'; #exit
			elif jSmall:
				if maze[i][j+1] != currentPosition:
					row += '   |';
				else:
					row += '    '; #4 spaces
			else:
				row += '   |'; 

			#if i, j in path: change two chars from end of row to letter. 
			if path and (i, j) in path:
				step = getAlphabetStep(path.index((i, j)));
				rowLen = len(row);
				row = row[0: rowLen - 3] + step + row[rowLen - 2:];
			
			if iSmall:
				if maze[i+1][j] != currentPosition:
					rowFloor += '---:';
				else:
					rowFloor += '   :';

		print(row);
		if iSmall: print(rowFloor);
		row = '';
		rowFloor = '';
	print(bottomRow);

#return the character of position index in the alphabet (with a = 0). 
def getAlphabetStep(index):
	return str(chr(ord('a') + index));


#Command line argument is size of the maze. 

mazeSize = int(sys.argv[1]);
while mazeSize == 1:
	print('C\'mon, that\'s not a maze.');
	mazeSize = int(input('Enter another size: '));

path = [];
#keep making random mazes until we find one with a path from the top left
#corner to the bottom right corner. 
while not path:
	maze = makeMaze(mazeSize);
	graph = makeGraph(parseGrid(maze));
	path = bfs((0, 0), (mazeSize - 1, mazeSize - 1), graph);

print '';
printMaze(maze, False);
print '';
print 'solution:'
printMaze(maze, path);