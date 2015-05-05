import sys
import maze

def makeMazeSolvable(maze):
	mazeSize = len(maze[0]);

	for j in range(mazeSize):
		maze[0][j] = 1;

	for i in range(mazeSize):
		maze[i][0] = 0;

	return maze;



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
	

if __name__ == "__main__":
	main()

	
