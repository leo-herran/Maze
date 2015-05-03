import random
import sys

def makeMaze(rowLength):
	grid = [];
	for i in range(rowLength):
		grid.append(makeRandomRow(rowLength));
	
	return grid;


def makeRandomRow(rowLength):
	row = [];
	for i in range(rowLength):
		if bool(random.getrandbits(1)):
			row.append('.');
		else: 
			row.append('0');

	return row;


#Finds and returns all pairs of horizontally/vertically adjacent 0s. 
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


def bfs(start, end, graph):
	stack = [(start, [start])];

	while stack:
		(node, path) = stack.pop();
		
		if node in graph:
			for nextNode in graph[node]:
				if not nextNode in set(path):
					if nextNode == end:
						return path + [nextNode];
					else:
						stack.append((nextNode, path + [nextNode]));

	return False


def printMaze(maze):
	for i in range(mazeSize):
		print(maze[i]);



#Command line argument is size of the maze. 
mazeSize = int(sys.argv[1]);
path = [];

#keep making random mazes until we find one with a path from the top left
#corner to the bottom right corner. 
while not path:
	maze = makeMaze(mazeSize);
	graph = makeGraph(parseGrid(maze));
	path = bfs((0, 0), (mazeSize - 1, mazeSize - 1), graph);

printMaze(maze);
print(path);